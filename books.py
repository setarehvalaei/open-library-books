import requests
import csv

url = "https://openlibrary.org/search.json?q=python&limit=50"

response = requests.get(url)

data = response.json()

books = data["docs"]

filtered_books = []

for book in books:
    year = book.get("first_publish_year")

    if year is not None and year >= 2000:
        filtered_books.append(book)

filtered_books.sort(
    key=lambda book: book.get("first_publish_year")
)

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["title", "author", "year"])

    for book in filtered_books:
        title = book.get("title")
        author = ", ".join(book.get("author_name", []))
        year = book.get("first_publish_year")

        writer.writerow([title, author, year])