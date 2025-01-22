from sudachipy import tokenizer
from sudachipy import dictionary
import pykakasi

# Initialize Sudachi and pykakasi
tokenizer_obj = dictionary.Dictionary().create()
kakasi = pykakasi.kakasi()

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
    tokens = tokenizer_obj.tokenize(sentence, tokenizer.Tokenizer.SplitMode.C)
    chunks = []
    for token in tokens:
        pos = token.part_of_speech()[0]  # Part of speech
        word = token.surface()  # Original word
        lemma = token.dictionary_form()  # Base form
        kana = token.reading_form()  # Kana pronunciation
        color = COLORS.get(pos, "gray")

        # Convert Kana to Romaji
        romaji_result = kakasi.convert(kana or "")
        romaji = romaji_result[0]["hepburn"] if romaji_result else "N/A"

        chunks.append({
            "text": word,
            "lemma": lemma,
            "kana": kana,
            "romaji": romaji,
            "role": pos,
            "color": color
        })
    return chunks
