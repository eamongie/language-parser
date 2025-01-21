import spacy

# Load Japanese NLP model
nlp = spacy.blank("ja")

# Color mapping for parts of speech
COLORS = {
    "NOUN": "blue",
    "VERB": "green",
    "ADJ": "red",
    "PART": "purple",
}

def parse_sentence(sentence):
    doc = nlp(sentence)
    tokens = []
    for token in doc:
        tokens.append({
            "text": token.text,
            "pos": token.pos_,
            "color": COLORS.get(token.pos_, "black")
        })
    return tokens
