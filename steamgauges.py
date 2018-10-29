# imported libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import time

start = time.time()

# define a url
quote_page = "https://steamgaug.es/api/v2"

# query and return html
page = urllib.request.urlopen(quote_page)

# parse the html and store in 'soup'
soup = BeautifulSoup(page, 'html.parser')
api = soup.text
print(api)


def status():
    regex = r"(?<=online\":\s)(.*)(?=)"
    matches = re.finditer(regex, api, re.MULTILINE)
    output = []

    for match in matches:
        string = match.group()
        string = string.replace(r",", r"")
        string = string.replace("1", "Online")
        string = string.replace("2", "Offline")
        string = string.replace("0", "Error")
        output.append(string)
        print(string)
    return output


print("""Steam Store: {}
Steam Community: {}
User API: {}
TF2:
Dots 2:
CSGO: """.format(status()[2], status()[1], status()[3]))

print(time.time() - start)
