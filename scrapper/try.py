import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the URL of the home page
url = "https://python.langchain.com/en/latest/index.html"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all anchor tags (<a>) with the specified class
anchor_tags = soup.find_all("a", class_="menu__link menu__link--sublist")

# List to store the sublinks
sublinks = []

# Extract the sublinks
for tag in anchor_tags:
    sublink = tag.get("href")
    if sublink and not sublink.startswith("#"):  # Exclude anchor links
        absolute_url = urljoin(url, sublink)
        sublinks.append(absolute_url)

# Print and see the sublinks
for sublink in sublinks:
    print(sublink)

'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import re
import os


# Inicjalizacja opcji przeglądarki
options = Options()
options.add_argument("--headless")  # Uruchom przeglądarkę w trybie bezgłowym (bez wyświetlania okna)

# Inicjalizacja usługi przeglądarki
service = Service("path/to/chromedriver")  # Podaj ścieżkę do chromedriver

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(service=service, options=options)

# Wczytaj stronę internetową
driver.get("https://python.langchain.com/en/latest/index.html")

# Poczekaj na załadowanie się strony i generację linków dynamicznych
time.sleep(5)  # Możesz dostosować czas oczekiwania w sekundach

# Pobierz linki
links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
list_links = [link.get_attribute("href") for link in links]

# Wyświetl linki
print(list_links)

def add_base_path(website_link, list_links):
    list_links_with_base_path = []

    for link in list_links:

        if not link.startswith('/'):
            link_with_base_path = website_link + link
            list_links_with_base_path.append(link_with_base_path)

  # if link.startswith('https://') dont add base path
        elif link.startswith('https://'):
            list_links_with_base_path.append(link)

        elif link.startswith('.'):
            link_with_base_path = website_link + link.split('/')[-1]
            list_links_with_base_path.append(link_with_base_path)

    return list_links_with_base_path

link_list = add_base_path('https://python.langchain.com/en/latest/', sub_links)
link_list_print = print(link_list)




# Zamknij przeglądarkę
driver.quit()
'''