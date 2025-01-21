import spacy

# Load Japanese NLP model
nlp = spacy.blank("ja")

# Color mapping for parts of speech
COLORS = {
    "NOUN": "blue",
    "VERB": "green",
    "ADJ": "red",
    "PART": "purple",
    "CONJ": "orange",
    "ADV": "teal",
    "PRON": "pink",
    "AUX": "brown",
    "INTJ": "lime",
}

def parse_sentence(sentence):
    doc = nlp(sentence)
    tokens = []
    for token in doc:
        tokens.append({
            "text": token.text,
            "pos": token.pos_,
            "color": COLORS.get(token.pos_, "black"),
        })
    return tokens

def get_base_form(word, pos):
    # Simplified logic for extracting base form (can integrate MeCab or SudachiPy)
    if pos == "VERB":
        # Placeholder logic for conjugation removal
        return word.rstrip("ます")  # Example: "行きます" -> "行く"
    return word
