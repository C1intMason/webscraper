# imported libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import math
import time
import xlsxwriter


# Listing Class, Each object represents a single listing
class Listing:
    def __init__(self, number, url_listing, title):
        self.number = number
        self.url_listing = url_listing
        self.title = title

    def show_url(self):
        return self.url_listing

    def settitle(self, title):
        self.title = title

    def show_title(self):
        return self.title


# Defines an empty list in order to fill with instances of "Listing"
listings = []


def run(page_number, total):
    print("Scraping Page # {} out of {}".format(page_number + 1, total))

    # define a url
    quote_page = "https://vancouver.craigslist.ca/search/cps?s={}".format(page_number*120)

    # query and return html
    page = urllib.request.urlopen(quote_page)

    # parse the html and store in 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # Puts URL of all listings into 'url_listings'
    url_listings = [a['href'] for a in soup.findAll('a', attrs={'class': 'result-title'})]

    print("Creating Instances!")
    # Creates instances of Listing and adds an URL
    for i in range(len(url_listings)):
        listings.append(Listing(i, url_listings[i], None))

    print("Finished creating instances!")
    # Adds titles to each instance of Listing
    for i in range(len(listings)):
        quote_page = listings[i].url_listing

        # query and return html
        page = urllib.request.urlopen(quote_page)

        # parse the html and store in 'soup'
        soup = BeautifulSoup(page, 'html.parser')

        title_listing = soup.title.extract()
        title_listing = title_listing.string

        listings[i].settitle(title_listing)

        completion = (i+1) / len(listings)
        completion = math.ceil(completion * 100)
        print("{}% finished... ({} out of {})".format(completion, (i+1), len(listings)))

    print("Finished!")

    book = xlsxwriter.Workbook("page{}.xlsx".format(page_number + 1))
    sheet = book.add_worksheet()
    bold = book.add_format({'bold': True})

    print("Dumping Data!")
    for i in range(len(listings)):
        print("[Title]:{} [URL]:{}".format(listings[i].show_title(), listings[i].show_url()))
        sheet.write(i, 0, listings[i].show_title())
        sheet.write(i, 6, listings[i].show_url())
        sheet.set_column(i, i, 10)


print("Craigslist Computer Services Web Scraper by Kevin Zhao")
time.sleep(1)
number_of_pages = int(input("How many pages would you like to scrape?"))
number_of_pages = number_of_pages - 1

for i in range(number_of_pages + 1):
    run(i, number_of_pages + 1)

