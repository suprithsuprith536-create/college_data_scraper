import requests
from bs4 import BeautifulSoup
import csv

# Sample NIRF Engineering ranking page
URL = "https://www.nirfindia.org/2023/EngineeringRanking.html"

def get_college_data():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    colleges = []

    table = soup.find("table")
    rows = table.find_all("tr")[1:]  # skip header

    for row in rows:
        cols = row.find_all("td")
        
        if len(cols) < 3:
            continue
        
        rank = cols[0].text.strip()
        name = cols[1].text.strip()

        # Placeholder values (extend later)
        naac = "NA"
        nba = "NA"
        year = "NA"
        college_type = "NA"
        affiliation = "NA"

        colleges.append([
            name, naac, nba, rank, "NIRF 2023", year, affiliation, college_type
        ])

    return colleges


def save_to_csv(data):
    with open("colleges.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow([
            "College Name", "NAAC", "NBA", "NIRF",
            "Other Rankings", "Year of Foundation",
            "Autonomous/University/VTU", "Type"
        ])
        
        writer.writerows(data)


if __name__ == "__main__":
    data = get_college_data()
    save_to_csv(data)
    print("✅ Data saved to colleges.csv")
