from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from time import sleep
import pathlib


BASEDIR = pathlib.Path(__file__).parent
print("Basedir: ", BASEDIR)

def task6():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get("https://owasp.org/www-project-top-ten/")
    sleep(3)


    elements = driver.find_elements(
        By.XPATH, "/html/body/main/div/div[1]/section[1]/ul[2]/li/a"
    )

    top_10 = []
    for element in elements:
        title = element.text.strip()
        href = element.get_attribute("href")
        top_10.append({"title": title, "link": href})


    for item in top_10:
        print(item)


    with open(BASEDIR / "owasp_top_10.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(top_10)


    driver.quit()

if __name__ == "__main__":
    task6()