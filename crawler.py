import json
import os
import re
from bs4 import BeautifulSoup
import requests

documents = {}
inverted_index = {}
doc_counter = 0

def add_document(url, text):
    global doc_counter
    documents[str(doc_counter)] = {"url": url, "text": text}
    words = re.findall(r"\w+", text.lower())
    for word in set(words):
        inverted_index.setdefault(word, []).append(doc_counter)
    doc_counter += 1

def crawl_page(url, depth=1, visited=None):
    if visited is None:
        visited = set()
    if url in visited or depth < 0:
        return
    visited.add(url)
    try:
        res = requests.get(url, timeout=15, headers={"User-Agent": "TescaBot/1.0"})
        res.raise_for_status()
        soup = BeautifulSoup(res.content, "html.parser")  # bytes: lets bs4 detect the charset
        text = soup.get_text(separator=" ", strip=True)
        add_document(url, text)
        print(f"Indexed: {url}")
        if depth > 0:
            links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("http")]
            for link in links[:10]:
                crawl_page(link, depth - 1, visited)
    except Exception as e:
        print(f"Skipped {url}: {e}")

if __name__ == "__main__":
    seeds = [
        "https://wikipedia.org",
        "https://bbc.com",
        "https://nationalgeographic.com",
    ]
    visited = set()
    for s in seeds:
        crawl_page(s, depth=1, visited=visited)

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump({"documents": documents, "inverted_index": inverted_index}, f, ensure_ascii=False)
    print(f"Success! Saved {len(documents)} pages to index.json")
