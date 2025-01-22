import requests

WIKTIONARY_API = "https://en.wiktionary.org/w/api.php"

def fetch_definition(word, lang="ja"):
    """Fetch the definition of a word from Wiktionary."""
    params = {
        "action": "query",
        "titles": word,
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
    }
    response = requests.get(WIKTIONARY_API, params=params)
    if response.status_code == 200:
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        for _, page in pages.items():
            if "extract" in page:
                return page["extract"]
    # Fallback message
    return f"No definition found for {word}."
