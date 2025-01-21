import streamlit as st
from parser import parse_sentence, get_base_form
from dictionary_lookup import fetch_word_data

# Set page title
st.set_page_config(page_title="Language Parser", layout="wide")

# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Input sentence
sentence = st.text_input("Enter a Japanese sentence:")

if sentence:
    # Parse the sentence
    tokens = parse_sentence(sentence)
    
    # Display parsed sentence with hover functionality
    st.markdown('<div class="sentence">', unsafe_allow_html=True)
    for token in tokens:
        base_form = get_base_form(token["text"], token["pos"])
        word_data = fetch_word_data(base_form)
        tooltip = f"""
            <div class='tooltip'>
                <strong>{word_data['word']}</strong><br>
                Pronunciation: {word_data.get('pronunciation', 'N/A')}<br>
                Part of Speech: {word_data.get('part_of_speech', 'N/A')}<br>
                Definition: {word_data.get('definition', 'N/A')}<br>
                Etymology: {word_data.get('etymology', 'N/A')}<br>
                Example: {word_data.get('example', 'N/A')}<br>
            </div>
        """
        st.markdown(
            f"<span class='word' style='color:{token['color']}' title='{tooltip}'>{token['text']}</span>",
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)
