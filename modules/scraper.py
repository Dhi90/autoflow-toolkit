import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime

def scrape_website(config_path: str, *_):
    url = input("Enter the website URL to scrape: ").strip()
    print(f"[INFO] Scraping URL: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        text = soup.get_text()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        phones = re.findall(r"\b\d{10,12}\b", text)
        links = [a['href'] for a in soup.find_all('a', href=True)]

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("output", exist_ok=True)
        output_path = f"output/scrape_{timestamp}.txt"

        with open(output_path, "w") as f:
            f.write(f"Scraped from: {url}\n\n")
            f.write("Emails:\n" + "\n".join(set(emails)) + "\n\n")
            f.write("Phones:\n" + "\n".join(set(phones)) + "\n\n")
            f.write("Links:\n" + "\n".join(set(links)) + "\n")

        print(f"[SUCCESS] Scraping complete. Output saved to: {output_path}")
    
    except Exception as e:
        print(f"[ERROR] Failed to scrape site: {e}")
