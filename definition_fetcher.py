import requests
from bs4 import BeautifulSoup
import fugashi

# Initialize Fugashi
tagger = fugashi.Tagger()

# Tangorin API details
TANGORIN_API_KEY = "YOUR_API_KEY"
TANGORIN_API_URL = "https://api.tangorin.com/v1/words"

# Dictionary fetch functions
def fetch_wiktionary(word):
    """Fetch definition from Wiktionary."""
    url = f"https://en.wiktionary.org/wiki/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        japanese_section = soup.find("span", {"id": "Japanese"})
        if japanese_section:
            content = []
            for sibling in japanese_section.find_parent().find_next_siblings():
                if sibling.name == "h2" and sibling.find("span", {"class": "mw-headline"}):
                    break
                content.append(sibling.get_text(strip=True))
            return "\n".join(content)
    return None

def fetch_tangorin(word):
    """Fetch definition from Tangorin."""
    params = {"q": word, "apikey": TANGORIN_API_KEY}
    response = requests.get(TANGORIN_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return "\n".join([f"{entry['word']}: {entry['definition']}" for entry in data])
    return None

def fetch_kanjipedia(word):
    """Fetch definition from Kanjipedia."""
    url = f"https://www.kanjipedia.jp/search?k={word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("div", class_="kanjiDetails")
        if result:
            return result.get_text(strip=True)
    return None

def fetch_unidic(word):
    """Fetch morphological information from Unidic."""
    tokens = [token for token in tagger(word)]
    if tokens:
        token = tokens[0]
        return f"{token.surface}: {token.feature.lemma}, Pronunciation: {token.feature.pron}"
    return None

# Combined fetch function
def fetch_definition(word):
    """Fetch definitions from online sources."""
    definitions = []

    # Wiktionary
    wiktionary_def = fetch_wiktionary(word)
    if wiktionary_def:
        definitions.append(f"**Wiktionary**\n{wiktionary_def}")

    # Tangorin
    tangorin_def = fetch_tangorin(word)
    if tangorin_def:
        definitions.append(f"**Tangorin**\n{tangorin_def}")

    # Kanjipedia
    kanjipedia_def = fetch_kanjipedia(word)
    if kanjipedia_def:
        definitions.append(f"**Kanjipedia**\n{kanjipedia_def}")

    # Unidic
    unidic_def = fetch_unidic(word)
    if unidic_def:
        definitions.append(f"**Unidic**\n{unidic_def}")

    # No definitions found
    if not definitions:
        definitions.append("No definition found.")

    return "\n\n".join(definitions)
