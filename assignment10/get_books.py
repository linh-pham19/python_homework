
from datetime import date
import pathlib
from typing import Dict, List
import pandas as pd
import json
from math import ceil
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

BASEDIR = pathlib.Path(__file__).parent
print("Basedir: ", BASEDIR)


def get_page_results(driver: webdriver) -> List[Dict]:
    
    results: List[Dict] = []

    body = driver.find_element(By.CSS_SELECTOR, "body")
    if body:
        search_elements = body.find_elements(
            By.CSS_SELECTOR, "li.row"
        )  # the search result elements
        for element in search_elements:

            element_dict = {}

            title = element.find_elements(By.CSS_SELECTOR, ".title-content")
            if len(title) > 0:
                element_dict["Title"] = title[0].text
            else:
                element_dict["Title"] = "Unknown"

            authors = element.find_elements(By.CSS_SELECTOR, ".author-link")
            authors_list: List[str] = []
            if len(authors) > 0:
                for author in authors:
                    authors_list.append(author.text)
                element_dict["Author"] = ";".join(authors_list)
            else:
                element_dict["Author"] = "Unknown"

            format = element.find_elements(By.CSS_SELECTOR, ".display-info-primary")
            if len(format) > 0:
                element_dict["Format-Year"] = format[0].text
            else:
                element_dict["Format-Year"] = "Unknown"

            results.append(element_dict)

    return results


def get_all_search_results(base_url) -> List[Dict]:

    # Initialize the web driver

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(base_url)

    body = driver.find_element(By.CSS_SELECTOR, "body")
    if body:
        pagination = body.find_elements(By.CSS_SELECTOR, ".cp-pagination-label")
        if len(pagination) > 0:
            pagination_text = pagination[0].text
            # Str Format: 1 to 20 of 269 results

            pagination_info = pagination_text.split()
            # Format:  ['1', 'to', '20', 'of', '269', 'results']

            page_length = 1 + int(pagination_info[2]) - int(pagination_info[0])
            total = int(pagination_info[4])

            number_of_steps = ceil(total / page_length)

    all_results: List[Dict] = []

    for page_number in range(1, number_of_steps + 1):
        print(
            f"Processing Page {page_number} and Result Items {(page_number-1)*page_length + 1} to {page_number*page_length}",
            end="\r",
        )
        driver.get(base_url + f"&page={page_number}")
        page_results = get_page_results(driver)
        all_results.extend(page_results)

        sleep(2)

        print(
            f"Finished Processing Page: {page_number}                                  "
        )

    driver.close()
    return all_results


if __name__ == "__main__":
    search_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

    results = get_all_search_results(search_url)
    df = pd.DataFrame(results)

    print("\nSearch Results\n")
    print(df.head(20))

    print("\nAll Results have been processed.")

    df.to_csv(BASEDIR / "get_books.csv")
    with open(BASEDIR / "get_books.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Finished Writing to disk.")