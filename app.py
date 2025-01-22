import streamlit as st
from chunker import chunk_sentence
from openai_helper import analyze_chunks
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App configuration
st.set_page_config(page_title="Japanese NLP Parser", layout="wide")

# Page title
st.title("Japanese NLP Parser")

# Input box for the sentence
sentence = st.text_input("Enter a Japanese sentence:")

if sentence:
    # Display loading spinner while processing
    with st.spinner("Processing the sentence..."):
        # Chunk the sentence into logical parts
        chunks = chunk_sentence(sentence)

        # Analyze chunks using OpenAI API
        analyzed_chunks = analyze_chunks(chunks)

    # Display the sentence with chunk explanations
    st.markdown("### Sentence Breakdown")
    for chunk in analyzed_chunks:
        st.markdown(
            f"<span style='color:{chunk['color']}; font-size: 18px;'>"
            f"{chunk['text']}</span>: {chunk['explanation']}",
            unsafe_allow_html=True
        )
