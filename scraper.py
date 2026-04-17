import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://www.nirfindia.org/2023/EngineeringRanking.html"

def get_college_data():
    response = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
        verify=False
    )
    
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    
    if not table:
        print("❌ Table not found (site uses JavaScript)")
        return []

    rows = table.find_all("tr")[1:]

    colleges = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 2:
            continue

        rank = cols[0].text.strip()
        name = cols[1].text.strip()

        colleges.append([
            name, "NA", "NA", rank, "NIRF 2023", "NA", "NA", "NA"
        ])

    return colleges
