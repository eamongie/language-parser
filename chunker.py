from sudachipy import tokenizer
from sudachipy import dictionary

COLORS = {
    "名詞": "blue",
    "動詞": "green",
    "形容詞": "red",
    "助詞": "purple",
    "副詞": "teal",
    "その他": "gray",
}

def chunk_sentence(sentence):
    """Tokenize the sentence and normalize tokens."""
    tokenizer_obj = dictionary.Dictionary().create()
    tokens = tokenizer_obj.tokenize(sentence, tokenizer.Tokenizer.SplitMode.C)
    chunks = []
    for token in tokens:
        pos = token.part_of_speech()[0]  # Part of speech
        word = token.surface()  # Original token
        lemma = token.dictionary_form()  # Base form
        color = COLORS.get(pos, "gray")
        chunks.append({
            "text": word,
            "lemma": lemma,  # Use lemma for dictionary lookups
            "role": pos,
            "color": color
        })
    return chunks
