import streamlit as st
from parser import parse_sentence
from dictionary_lookup import fetch_definition

# Set page title
st.set_page_config(page_title="Language Parser", layout="wide")

# Input sentence
sentence = st.text_input("Enter a Japanese sentence:")

if sentence:
    # Parse the sentence
    tokens = parse_sentence(sentence)
    
    # Display results
    st.markdown("### Parsed Sentence")
    for token in tokens:
        st.markdown(
            f'<span style="color:{token["color"]};">{token["text"]}</span>',
            unsafe_allow_html=True
        )
        if st.button(f"Define {token['text']}"):
            definition = fetch_definition(token["text"])
            st.markdown(f"**{token['text']}:** {definition}")
