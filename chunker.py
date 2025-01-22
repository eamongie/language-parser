from sudachipy import tokenizer
from sudachipy import dictionary

# Color mapping for grammatical roles
COLORS = {
    "名詞": "blue",  # Noun
    "動詞": "green",  # Verb
    "形容詞": "red",  # Adjective
    "助詞": "purple",  # Particle
    "助動詞": "orange",  # Auxiliary verb
    "副詞": "teal",  # Adverb
    "感動詞": "pink",  # Interjection
    "その他": "gray",  # Default for unknown or other types
}

def chunk_sentence(sentence):
    tokenizer_obj = dictionary.Dictionary().create()
    tokens = tokenizer_obj.tokenize(sentence, tokenizer.Tokenizer.SplitMode.C)
    chunks = []
    for token in tokens:
        pos = token.part_of_speech()[0]  # Part of speech
        word = token.surface()  # Word surface form
        color = COLORS.get(pos, "gray")
        chunks.append({"text": word, "role": pos, "color": color})
    return chunks
