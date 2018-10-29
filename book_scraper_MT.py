# imported libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from multiprocessing import Pool


class Book:
    def __init__(self, url, name, price, upc):
        self.url = url
        self.name = name
        self.price = price
        self.upc = upc

    def get_info(self):
        return self.name, self.price, self.upc, self.url


def setup(url):
    return BeautifulSoup((urllib.request.urlopen(url)), "html.parser")


def get_book(page_number):
    instances = []
    print("Working on Page", page_number)
    soup = setup("http://books.toscrape.com/catalogue/page-{}.html".format(page_number))
    headings = soup.find_all("h3")  # Find all books by H3
    for h in headings:
        book = h.find_all("a")  # Get link tags of each book and store it
        for a in book:  # get the attribute of "a" tag
            url = a.get("href")
            url = ("http://books.toscrape.com/catalogue/"+url)
            soup_book = setup(url)
            tags = soup_book.find_all("td")
            name = soup_book.find("h1").contents
            name = "".join(name)
            attributes = []
            for att in tags:
                for i in att.contents:
                    attributes.append(i)
            instances.append(Book(url, name, attributes[2], attributes[0]))
    return instances


def pool_handler():
    p = Pool(1)
    pages = list(range(1, 2))  # TODO Only does page(s) 1
    result = p.map_async(get_book, pages)
    print(result.get()[0].__dict__)
    p.terminate()
    p.join()


if __name__ == "__main__":
    pool_handler()

