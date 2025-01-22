import fugashi
import pykakasi
import requests
from bs4 import BeautifulSoup

# Initialize tagger and romaji converter
tagger = fugashi.Tagger()
kakasi = pykakasi.kakasi()

# Wiktionary URL
WIKTIONARY_URL = "https://en.wiktionary.org/wiki/"

def fetch_wiktionary_definition(word):
    """Fetch the definition of a word from Wiktionary."""
    url = f"{WIKTIONARY_URL}{word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        japanese_heading = soup.find("span", {"id": "Japanese"})
        if japanese_heading:
            content = []
            for sibling in japanese_heading.find_parent().find_next_siblings():
                if sibling.name == "h2" and sibling.find("span", {"class": "mw-headline"}):
                    break
                content.append(sibling.get_text(strip=True))
            return "\n".join(content)
    return None

def fetch_jmdict_definition(word):
    """Fetch a definition from JMDict (mocked as an example)."""
    # Placeholder logic for JMDict integration
    # Replace with actual lookup if using pyglossary or jmdict-python
    mock_jmdict = {
        "小型": "Small-sized.",
        "旅客機": "Passenger aircraft.",
        "墜落": "Crash or fall."
    }
    return mock_jmdict.get(word)

def fetch_definition(word):
    """Fetch definitions with fallbacks."""
    definitions = []

    # Try Wiktionary
    wiktionary_def = fetch_wiktionary_definition(word)
    if wiktionary_def:
        definitions.append(f"**Wiktionary**\n{wiktionary_def}")

    # Try JMDict (mocked in this example)
    jmdict_def = fetch_jmdict_definition(word)
    if jmdict_def:
        definitions.append(f"**JMDict**\n{jmdict_def}")

    # If no definitions found
    if not definitions:
        definitions.append("No definition found.")

    return "\n\n".join(definitions)
