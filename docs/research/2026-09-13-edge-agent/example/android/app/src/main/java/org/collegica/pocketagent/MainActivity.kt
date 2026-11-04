package org.collegica.pocketagent

import android.app.Activity
import android.os.Bundle
import android.os.SystemClock
import android.text.method.ScrollingMovementMethod
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import com.google.ai.edge.litertlm.Backend
import com.google.ai.edge.litertlm.Contents
import com.google.ai.edge.litertlm.Conversation
import com.google.ai.edge.litertlm.ConversationConfig
import com.google.ai.edge.litertlm.Engine
import com.google.ai.edge.litertlm.EngineConfig
import com.google.ai.edge.litertlm.tool
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.File

/**
 * One screen: a question box, an Ask button, the answer, and the time it
 * took. The model file goes in the app's own external-files directory,
 * not /data/local/tmp: the GPU backend writes a weight-cache file next
 * to the model on first load, and shell's directory refuses that write
 * from an installed app ("Permission denied" on delegate_opencl.cc:340).
 *
 *   adb shell mkdir -p /sdcard/Android/data/org.collegica.pocketagent/files
 *   adb push gemma-4-E2B-it.litertlm /sdcard/Android/data/org.collegica.pocketagent/files/
 *
 * and the engine is created on a background thread because initialize()
 * can take seconds (measured: 7.1 s GPU, 3.4 s CPU, on a Galaxy S26
 * Ultra). Set useGpu to false to compare the CPU backend.
 */
class MainActivity : Activity() {
    private val modelPath = "/sdcard/Android/data/org.collegica.pocketagent/files/gemma-4-E2B-it.litertlm"
    private val useGpu = true
    private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
    private var engine: Engine? = null
    private var conversation: Conversation? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val pad = (16 * resources.displayMetrics.density).toInt()
        val status = TextView(this).apply { text = "Loading $modelPath…" }
        val question = EditText(this).apply {
            hint = "Ask about the unclassified rows"
            setText("Which outflows in 2026-08 are unclassified, and what did the cafe cost in total?")
        }
        val ask = Button(this).apply { text = "Ask"; isEnabled = false }
        val answer = TextView(this).apply { movementMethod = ScrollingMovementMethod() }
        setContentView(LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(pad, pad, pad, pad)
            addView(status); addView(question); addView(ask); addView(answer)
        })

        scope.launch {
            val t0 = SystemClock.elapsedRealtime()
            val result = runCatching {
                require(File(modelPath).exists()) { "no model at $modelPath — adb push it first" }
                val e = Engine(EngineConfig(
                    modelPath = modelPath,
                    backend = if (useGpu) Backend.GPU() else Backend.CPU(),
                ))
                e.initialize()
                engine = e
                conversation = e.createConversation(ConversationConfig(
                    systemInstruction = Contents.of(
                        "You are a careful bookkeeping assistant. Use the tools to answer; " +
                        "never invent a figure. If a category is unclear, say so."),
                    tools = listOf(tool(StatementTools())),
                ))
            }
            val ms = SystemClock.elapsedRealtime() - t0
            withContext(Dispatchers.Main) {
                status.text = result.fold(
                    { "Ready on ${if (useGpu) "GPU" else "CPU"} in $ms ms" },
                    { "Failed: ${it.message}" })
                ask.isEnabled = result.isSuccess
            }
        }

        ask.setOnClickListener {
            ask.isEnabled = false
            answer.text = "…"
            val q = question.text.toString()
            scope.launch {
                val t0 = SystemClock.elapsedRealtime()
                val text = runCatching { conversation!!.sendMessage(q).toString() }
                    .getOrElse { "Failed: ${it.message}" }
                val ms = SystemClock.elapsedRealtime() - t0
                withContext(Dispatchers.Main) {
                    answer.text = "$text\n\n[$ms ms, tools called automatically]"
                    ask.isEnabled = true
                }
            }
        }
    }

    override fun onDestroy() {
        conversation?.close(); engine?.close()
        super.onDestroy()
    }
}
