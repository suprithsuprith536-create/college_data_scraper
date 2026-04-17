from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    return driver


def scrape_nirf():
    url = "https://www.nirfindia.org/2023/EngineeringRanking.html"
    driver = get_driver()
    driver.get(url)

    time.sleep(5)  # allow JS to load

    rows = driver.find_elements(By.XPATH, "//table//tr")

    data = []

    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) < 2:
            continue

        rank = cols[0].text
        name = cols[1].text

        data.append({
            "College Name": name,
            "NAAC": "NA",
            "NBA": "NA",
            "NIRF": rank,
            "Other Rankings": "NIRF 2023",
            "Year of Foundation": "NA",
            "Autonomous/University/VTU": "NA",
            "Type": "NA"
        })

    driver.quit()
    return data
