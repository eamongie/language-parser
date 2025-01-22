import streamlit as st
import speech_recognition as sr

# Set custom style
st.markdown(
    """
    <link rel="stylesheet" href="static/style.css">
    """,
    unsafe_allow_html=True
)

def transcribe_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            st.info("Adjusting for ambient noise... Speak when ready.")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            st.info("Listening...")
            audio = recognizer.listen(source)

        st.info("Processing transcription...")
        transcription = recognizer.recognize_google(audio)
        return transcription

    except sr.UnknownValueError:
        return "Sorry, I could not understand that."
    except sr.RequestError as e:
        return f"Error with the Speech Recognition service: {e}"

# Streamlit UI
st.title("🎤 Real-Time Speech Transcription")
st.write("Click the button below to start transcribing from your microphone.")

if st.button("Start Transcription"):
    result = transcribe_from_microphone()
    st.write(f"### Transcription: `{result}`")
