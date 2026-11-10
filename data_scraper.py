# Data Scraper
# This program gets book titles and prices from a website made for practicing scraping.
import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    # 1. Get the web page
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # 2. Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Find all the books on the page
    books = soup.find_all("article", class_="product_pod")

    data = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        data.append([title, price])

    # 4. Save the data in a CSV file
    file = open("books.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(data)
    file.close()

    print("Scraped", len(data), "books and saved them in books.csv")

except requests.exceptions.RequestException:
    print("Error: could not get the web page")
