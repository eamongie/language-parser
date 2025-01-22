import streamlit as st
from chunker import chunk_sentence
from openai_helper import analyze_chunks

# Set up the page and load custom CSS
st.set_page_config(page_title="Japanese NLP Parser", layout="wide")
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Input box for the sentence
sentence = st.text_input("Enter a Japanese sentence:")

if sentence:
    # Chunk the sentence into logical parts
    chunks = chunk_sentence(sentence)

    # Analyze each chunk using the OpenAI API
    analyzed_chunks = analyze_chunks(chunks)

    # Display the sentence with color-coded chunks
    st.markdown('<div class="sentence">', unsafe_allow_html=True)
    for chunk in analyzed_chunks:
        tooltip = f"""
            <div class='tooltip'>
                <strong>{chunk['text']}</strong><br>
                <em>Role:</em> {chunk['role']}<br>
                <em>Explanation:</em> {chunk['explanation']}
            </div>
        """
        st.markdown(
            f"<span class='chunk' style='color:{chunk['color']}' title='{tooltip}'>{chunk['text']}</span>",
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)
