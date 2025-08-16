import whisper
import os

audio_path = input("Enter audio filepath: ")

modelo = whisper.load_model("base")
result = modelo.transcribe(audio, verbose=True)
# Save transcription to a text file
text = result.get("text", "")
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(text.strip())

# Also print to console
print(f"Transcription: {text.strip()}")
