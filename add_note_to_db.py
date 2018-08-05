import sys
from bs4 import BeautifulSoup
import sqlite3


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


def create_database(filename):
    conn = sqlite3.connect(filename)
    contracts_table = """ CREATE TABLE IF NOT EXISTS notes (
                                        id integer PRIMARY KEY,
                                        note text NOT NULL
                                    ); """
    c = conn.cursor()
    c.execute(contracts_table)
    return conn


def add_data(conn, note):
    insert_note = """ INSERT INTO notes(note)
              VALUES(?) """
    c = conn.cursor()
    data = (note,)
    c.execute(insert_note, data)
    conn.commit()
    return c.lastrowid


if __name__ == "__main__":
    text = extract_text(BeautifulSoup(sys.argv[1], "html.parser")) + "\n\n"
    dbconn = create_database("notes.db")
    add_data(dbconn, text)
