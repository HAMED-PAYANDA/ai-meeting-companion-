import torch
from transformers import pipeline

# Initialize the speech-to-text pipeline from Hugging Face Transformers
# Uses "openai/whisper-tiny.en" for automatic speech recognition
pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-tiny.en",
  chunk_length_s=30,
)

# Define path to the downloaded audio file
sample = 'downloaded_audio.mp3'

# Perform speech recognition
prediction = pipe(sample, batch_size=8)["text"]

# Print the transcribed text
print(prediction)
