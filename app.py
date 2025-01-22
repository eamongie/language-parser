import streamlit as st
from chunker import chunk_sentence
from definition_fetcher import fetch_definition

# Streamlit configuration
st.set_page_config(page_title="Japanese Sentence Parser", layout="wide")
st.title("Japanese Sentence Parser")

# Input box for the sentence
sentence = st.text_input("Enter a Japanese sentence:")

if sentence:
    # Parse the sentence
    with st.spinner("Processing the sentence..."):
        chunks = chunk_sentence(sentence)

    # Display sentence breakdown
    st.markdown("### Sentence Breakdown")
    sentence_romaji = []
    for chunk in chunks:
        # Fetch the definition for the lemma
        definition = fetch_definition(chunk["lemma"])
        sentence_romaji.append(chunk["romaji"])  # Collect romaji for the sentence
        st.markdown(
            f"<span style='color:{chunk['color']}; font-size: 18px;'>{chunk['text']}</span>: {definition}",
            unsafe_allow_html=True
        )

    # Display sentence-wide romaji
    st.markdown("### Sentence in Romaji")
    st.write(" ".join(sentence_romaji))
