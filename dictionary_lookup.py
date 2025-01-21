import requests

def fetch_definition(word):
    url = f"https://en.wiktionary.org/wiki/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Definition found at: {url}"
    else:
        return "Definition not found."
