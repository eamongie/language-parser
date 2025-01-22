import requests
from bs4 import BeautifulSoup

WIKTIONARY_URL = "https://en.wiktionary.org/wiki/"

def fetch_wiktionary_page(word):
    """Fetch the Wiktionary page HTML for a word."""
    url = f"{WIKTIONARY_URL}{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_japanese_section(html):
    """Extract the Japanese section from the Wiktionary page HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Locate the Japanese heading
    japanese_heading = soup.find("span", {"id": "Japanese"})
    if not japanese_heading:
        return "No Japanese section found."

    # Extract content under the Japanese heading
    japanese_content = []
    for sibling in japanese_heading.find_parent().find_next_siblings():
        # Stop if we reach another major heading
        if sibling.name == "h2" and sibling.find("span", {"class": "mw-headline"}):
            break
        japanese_content.append(str(sibling))

    return "\n".join(japanese_content)

def clean_japanese_section(content):
    """Clean and format the Japanese section content."""
    soup = BeautifulSoup(content, "html.parser")
    clean_text = []

    # Find key sections like Pronunciation, Noun, Verb, etc.
    for section in soup.find_all(["h3", "h4", "p", "ul"]):
        if section.name in ["h3", "h4"]:
            clean_text.append(f"**{section.get_text()}**")  # Format headings
        elif section.name in ["p", "ul"]:
            clean_text.append(section.get_text())  # Add content

    return "\n\n".join(clean_text)

def fetch_definition(word):
    """Fetch the definition of a word from Wiktionary."""
    html = fetch_wiktionary_page(word)
    if html:
        japanese_content = extract_japanese_section(html)
        if japanese_content and japanese_content != "No Japanese section found.":
            return clean_japanese_section(japanese_content)
    return f"No definition found for {word}."
