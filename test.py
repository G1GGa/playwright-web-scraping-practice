import csv
from playwright.sync_api import sync_playwright

#opern browser with playwright and http get request
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")

#find all selectors
    books = page.query_selector_all(".product_pod")
    box = []

#take elements from books list
    for element in books:
        dictionary = {
            "Title": element.query_selector("h3 a").get_attribute("title"),
            "Price": element.query_selector("p.price_color").inner_text()
        }
        box.append(dictionary)
#browser close
    browser.close()

#fill data in csv
fieldnames = ["Title", "Price"]
with open ("books.csv", "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(box)
