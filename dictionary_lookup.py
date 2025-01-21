import requests
from bs4 import BeautifulSoup

def fetch_word_data(word):
    url = f"https://en.wiktionary.org/wiki/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
            "word": word,
            "pronunciation": "N/A",  # Extract if available
            "part_of_speech": "N/A",  # Extract if available
            "definition": "N/A",  # Extract if available
            "etymology": "N/A",  # Extract if available
            "example": "N/A",  # Extract if available
        }
    else:
        return {
            "word": word,
            "pronunciation": "N/A",
            "part_of_speech": "N/A",
            "definition": "Definition not found.",
            "etymology": "N/A",
            "example": "N/A",
        }
