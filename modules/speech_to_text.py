import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

def record_audio(filename, duration=5, fs=44100):
    print("🎤 Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print("✅ Audio recorded.")

def transcribe_audio(audio_path):
    record_audio(audio_path)
    model = WhisperModel("base", compute_type="int8")
    segments, _ = model.transcribe(audio_path)
    return " ".join([segment.text for segment in segments])
