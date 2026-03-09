import requests
from bs4 import BeautifulSoup
import json
import argparse

def scrape_quotes(pages):
    all_quotes = []

    for page in range(1, pages + 1):
        url = f"http://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

            all_quotes.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

        print(f"Scraped page {page} — {len(quotes)} quotes found")

    return all_quotes

def save_to_json(data, filename="quotes.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(data)} quotes to {filename}")

parser = argparse.ArgumentParser(description="Quotes Web Scraper")
parser.add_argument("--pages", type=int, default=3, help="Number of pages to scrape")
parser.add_argument("--output", type=str, default="quotes.json", help="Output filename")
args = parser.parse_args()

quotes = scrape_quotes(args.pages)
save_to_json(quotes, args.output)