import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import os

# Set custom style
st.markdown(
    """
    <link rel="stylesheet" href="static/style.css">
    """,
    unsafe_allow_html=True
)

# Record audio function
def record_audio(duration=5, sample_rate=44100, filename="output.wav"):
    st.info(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    wav.write(filename, sample_rate, audio_data)
    st.success("Recording finished! Saved as output.wav.")
    return filename

# Transcribe audio function
def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        st.info("Transcribing audio...")
        audio = recognizer.record(source)
    try:
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Error with the Speech Recognition service: {e}"

# Streamlit UI
st.title("🎤 Real-Time Speech Transcription (Local Recording)")
st.write("Record your voice using the microphone and transcribe it into text.")

duration = st.slider("Recording Duration (seconds):", min_value=1, max_value=10, value=5)

if st.button("Start Recording"):
    audio_file = record_audio(duration)
    transcription = transcribe_audio(audio_file)
    st.write(f"### Transcription: `{transcription}`")

    # Optional: Delete the audio file after processing
    os.remove(audio_file)
