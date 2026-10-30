package org.collegica.pocketagent

import com.google.ai.edge.litertlm.Tool
import com.google.ai.edge.litertlm.ToolParam
import com.google.ai.edge.litertlm.ToolSet

/** The same two tools as the CLI preset (owl_tools.py): rows the model
 *  must ask for rather than invent. Four made-up rows; nothing personal. */
class StatementTools : ToolSet {
    private val rows = listOf(
        Triple("2026-08-03", "CHEQUE 0042", 1250.00),
        Triple("2026-08-05", "SQ *CAFE 4471", 6.40),
        Triple("2026-08-12", "NEWTOWN DENTAL", 180.00),
        Triple("2026-08-19", "SQ *CAFE 4471", 7.10),
    )

    @Tool(description = "Lists the outflows in a month that no rule has classified yet.")
    fun listUnclassified(
        @ToolParam(description = "The month as YYYY-MM, for example 2026-08.") month: String,
    ): List<Map<String, Any>> =
        rows.filter { it.first.startsWith(month) }
            .map { mapOf("date" to it.first, "description" to it.second, "amount" to it.third) }

    @Tool(description = "Adds up every outflow whose description contains the given text.")
    fun totalFor(
        @ToolParam(description = "Text to match, case-insensitively, such as CAFE.") description: String,
    ): Double =
        rows.filter { it.second.contains(description, ignoreCase = true) }.sumOf { it.third }
}
