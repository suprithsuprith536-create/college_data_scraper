import requests
from bs4 import BeautifulSoup
import pdfplumber

def fetch_webpage_text(url):
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.get_text(separator=" ", strip=True)
    except:
        return ""


def fetch_wikipedia_text(url):
    return fetch_webpage_text(url)


def extract_pdf_text(path):
    text = ""
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        pass
    return text
