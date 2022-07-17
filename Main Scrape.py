from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

html_data = requests.get("https://en.wikipedia.org/wiki/List_of_largest_banks").text

print(html_data[101:124])

