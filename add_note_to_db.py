import sys
from bs4 import BeautifulSoup

def extract_text(soup):
    if soup is None:
        return None
    for crap in soup(["script", "style", "meta"]):
        crap.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n\n'.join(chunk for chunk in chunks if chunk)
    return text

text = extract_text(BeautifulSoup(sys.argv[1], "html.parser")) + "\n\n"

with open("text.txt", 'a') as tt:
    tt.write(text)
