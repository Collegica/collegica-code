import glob, os, time, json
import numpy as np, soundfile as sf
T = {}
def tick(k, t0): T[k] = round(time.perf_counter() - t0, 3); return T[k]
def to16k(x, sr):
    if sr == 16000: return x.astype(np.float32)
    n = int(round(len(x) * 16000 / sr)); return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)
print("cpus:", os.cpu_count())

# --- TTS: Kokoro (ONNX, CPU) -------------------------------------------------
from kokoro_onnx import Kokoro
t0 = time.perf_counter(); kokoro = Kokoro("models/kokoro-v1.0.onnx", "models/voices-v1.0.bin"); tick("kokoro_load", t0)
SENT = "The quick brown fox jumps over the lazy dog, and the meeting moves to half past nine on Thursday."
t0 = time.perf_counter(); samples, sr = kokoro.create(SENT, voice="af_heart", speed=1.0, lang="en-us"); tick("kokoro_tts_first", t0)
t0 = time.perf_counter(); samples, sr = kokoro.create(SENT, voice="af_heart", speed=1.0, lang="en-us"); tick("kokoro_tts_second", t0)
dur = len(samples) / sr; T["kokoro_audio_seconds"] = round(dur, 2); T["kokoro_rtf"] = round(T["kokoro_tts_second"] / dur, 3)
sf.write("sentence_24k.wav", samples, sr); x16 = to16k(np.asarray(samples), sr); sf.write("sentence_16k.wav", x16, 16000)
t0 = time.perf_counter(); wake, wsr = kokoro.create("Hey Jarvis, what is the weather like today?", voice="am_michael", speed=1.0, lang="en-us"); tick("kokoro_tts_wake", t0)
w16 = to16k(np.asarray(wake), wsr); sf.write("wake_16k.wav", w16, 16000)
print(f"kokoro: {sr} Hz, {dur:.2f}s of audio in {T['kokoro_tts_second']}s (RTF {T['kokoro_rtf']})")

# --- VAD: Silero (ONNX, CPU) --------------------------------------------------
from silero_vad import load_silero_vad, get_speech_timestamps
import torch
t0 = time.perf_counter(); vad = load_silero_vad(onnx=True); tick("silero_load", t0)
t0 = time.perf_counter(); ts = get_speech_timestamps(torch.from_numpy(x16), vad, sampling_rate=16000, return_seconds=True); tick("silero_vad", t0)
print("silero speech segments:", ts)

# --- STT: sherpa-onnx, three models ------------------------------------------
import sherpa_onnx
def g(p): m = glob.glob(p); assert m, p; return m[0]
W = "models/sherpa-onnx-whisper-tiny.en"; M = "models/sherpa-onnx-moonshine-tiny-en-int8"; Z = "models/sherpa-onnx-streaming-zipformer-en-2023-06-26"
t0 = time.perf_counter()
whisper = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=g(f"{W}/*encoder.int8.onnx"), decoder=g(f"{W}/*decoder.int8.onnx"), tokens=g(f"{W}/*tokens.txt"), num_threads=4, language="en", task="transcribe")
tick("whisper_load", t0)
for k in ("whisper_first", "whisper_second"):
    t0 = time.perf_counter(); s = whisper.create_stream(); s.accept_waveform(16000, x16); whisper.decode_stream(s); tick(k, t0); wtext = s.result.text
print(f"whisper-tiny.en (int8): {T['whisper_second']}s -> {wtext!r}")
t0 = time.perf_counter()
moon = sherpa_onnx.OfflineRecognizer.from_moonshine(preprocessor=g(f"{M}/preprocess*.onnx"), encoder=g(f"{M}/encode*.onnx"), uncached_decoder=g(f"{M}/uncached_decode*.onnx"), cached_decoder=g(f"{M}/cached_decode*.onnx"), tokens=g(f"{M}/tokens.txt"), num_threads=4)
tick("moonshine_load", t0)
for k in ("moonshine_first", "moonshine_second"):
    t0 = time.perf_counter(); s = moon.create_stream(); s.accept_waveform(16000, x16); moon.decode_stream(s); tick(k, t0); mtext = s.result.text
print(f"moonshine-tiny (int8): {T['moonshine_second']}s -> {mtext!r}")
t0 = time.perf_counter()
zip_ = sherpa_onnx.OnlineRecognizer.from_transducer(tokens=g(f"{Z}/tokens.txt"), encoder=g(f"{Z}/encoder*chunk-16-left-128.onnx"), decoder=g(f"{Z}/decoder*chunk-16-left-128.onnx"), joiner=g(f"{Z}/joiner*chunk-16-left-128.onnx"), num_threads=4, sample_rate=16000, feature_dim=80, enable_endpoint_detection=True)
tick("zipformer_load", t0)
# streaming: feed 100 ms chunks as if live; measure compute per chunk and the tail after the last chunk (1 s of silence closes the last word)
chunk = 1600; per = []; s = zip_.create_stream(); t_all = time.perf_counter()
for i in range(0, len(x16), chunk):
    t0 = time.perf_counter(); s.accept_waveform(16000, x16[i:i+chunk])
    while zip_.is_ready(s): zip_.decode_stream(s)
    per.append(time.perf_counter() - t0)
t0 = time.perf_counter(); s.accept_waveform(16000, np.zeros(int(1.0*16000), dtype=np.float32)); s.input_finished()
while zip_.is_ready(s): zip_.decode_stream(s)
tick("zipformer_tail", t0); ztext = zip_.get_result(s)
T["zipformer_total"] = round(time.perf_counter() - t_all, 3); T["zipformer_ms_per_100ms_chunk"] = round(1000*float(np.mean(per)), 1); T["zipformer_max_ms_chunk"] = round(1000*float(np.max(per)), 1)
print(f"streaming zipformer: {T['zipformer_ms_per_100ms_chunk']} ms compute per 100 ms chunk (max {T['zipformer_max_ms_chunk']}), total {T['zipformer_total']}s -> {ztext!r}")

# --- Wake word: openWakeWord on the Kokoro-spoken 'Hey Jarvis' ---------------
import openwakeword
from openwakeword.model import Model
# uv resolved openwakeword 0.4.0 on Python 3.12 (newer releases pin tflite-runtime, which has no 3.12 wheel);
# 0.4.0 ships the pre-trained models inside the package and takes model paths, not names
t0 = time.perf_counter(); oww = Model(wakeword_model_paths=[os.path.join(os.path.dirname(openwakeword.__file__), "resources", "models", "hey_jarvis_v0.1.onnx")]); tick("oww_load", t0)
frame = 1280; best = 0.0; first_hit = None; per = []
w16i = (np.clip(w16, -1, 1) * 32767).astype(np.int16)
for i in range(0, len(w16i) - frame, frame):
    t0 = time.perf_counter(); sc = oww.predict(w16i[i:i+frame]); per.append(time.perf_counter() - t0)
    v = float(list(sc.values())[0]); best = max(best, v)
    if first_hit is None and v > 0.5: first_hit = round((i + frame) / 16000, 2)
T["oww_best_score"] = round(best, 3); T["oww_first_hit_s"] = first_hit; T["oww_ms_per_80ms_frame"] = round(1000*float(np.mean(per)), 2)
print(f"openWakeWord hey_jarvis: best score {best:.3f}, crossed 0.5 at {first_hit}s of audio, {T['oww_ms_per_80ms_frame']} ms per 80 ms frame")
print(json.dumps(T, indent=1))
