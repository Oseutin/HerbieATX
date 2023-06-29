# code modified by Austin Fang and Amulya Bhattaram for Herbie 2.0
# references Whisper GitHub at https://github.com/openai/whisper
# references code from Ryan O'Connor at https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/

import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)