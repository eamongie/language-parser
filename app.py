import streamlit as st
from chunker import chunk_sentence
from definition_fetcher import fetch_definition

# App configuration
st.set_page_config(page_title="Japanese Sentence Parser", layout="wide")

# Page title
st.title("Japanese Sentence Parser")

# Input box for the sentence
sentence = st.text_input("Enter a Japanese sentence:")

if sentence:
    # Parse the sentence
    with st.spinner("Parsing the sentence..."):
        chunks = chunk_sentence(sentence)

    # Fetch definitions for each token
    st.markdown("### Sentence Breakdown")
    for chunk in chunks:
        definition = fetch_definition(chunk["text"])
        st.markdown(
            f"<span style='color:{chunk['color']}; font-size: 18px;'>{chunk['text']}</span>: {definition}",
            unsafe_allow_html=True
        )
