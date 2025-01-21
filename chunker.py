import spacy

# Load English model (modify for Japanese)
nlp = spacy.load("en_core_web_sm")

# Color mapping for grammatical roles
COLORS = {
    "Subject": "blue",
    "Verb": "green",
    "Object": "orange",
    "Adverb": "purple",
    "Other": "gray"
}

def chunk_sentence(sentence):
    doc = nlp(sentence)
    chunks = []
    for token in doc:
        if token.dep_ == "nsubj":
            chunks.append({"text": token.text, "role": "Subject", "color": COLORS["Subject"]})
        elif token.pos_ == "VERB":
            chunks.append({"text": token.text, "role": "Verb", "color": COLORS["Verb"]})
        elif token.dep_ == "dobj" or token.dep_ == "pobj":
            chunks.append({"text": token.text, "role": "Object", "color": COLORS["Object"]})
        elif token.pos_ == "ADV":
            chunks.append({"text": token.text, "role": "Adverb", "color": COLORS["Adverb"]})
        else:
            chunks.append({"text": token.text, "role": "Other", "color": COLORS["Other"]})
    return chunks
