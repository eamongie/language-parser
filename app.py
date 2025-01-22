import streamlit as st
from chunker import chunk_sentence
from definition_fetcher import fetch_definition

st.title("Japanese Sentence Parser")

sentence = st.text_input("Enter a Japanese sentence:")
if sentence:
    with st.spinner("Processing..."):
        chunks = chunk_sentence(sentence)

    st.markdown("### Sentence Breakdown")
    for chunk in chunks:
        definition = fetch_definition(chunk["lemma"])
        st.markdown(
            f"<span style='color:{chunk['color']}; font-size: 18px;'>{chunk['text']}</span>: {definition}",
            unsafe_allow_html=True
        )
