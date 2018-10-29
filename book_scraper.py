# imported libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup


class Book:
    def __init__(self, url, name, price, genre, upc):
        self.url = url
        self.name = name
        self.price = price
        self.genre = genre
        self.upc = upc

    def get_info(self):
        return self.name, self.price, self.genre, self.upc, self.url


def setup(url):
    return BeautifulSoup((urllib.request.urlopen(url)), "html.parser")


books = []


def run(page_number):
    soup = setup("http://books.toscrape.com/catalogue/page-{}.html".format(page_number))
    headings = soup.find_all("h3")
    for h in headings:
        page = h.find_all("a")
        for a in page:
            url = a.get("href")
            url = ("http://books.toscrape.com/catalogue/"+url)
            books.append(Book(url, None, None, None, None))

    for book in books:
        attributes = []
        soup = setup(book.url)
        tags = soup.find_all("td")
        name = soup.find("h1").contents
        name = "".join(name)
        for att in tags:
            for i in att.contents:
                attributes.append(i)
        book.name = name
        book.genre
        book.price = attributes[2]
        book.upc = attributes[0]
        # print(book.__dict__)


for i in range(1, 50):
    print("Scraping page {} out of {}".format(i, 50))
    run(i)

for book in books:
    print(book.get_info())
