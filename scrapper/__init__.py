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

'''
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
'''



# Zamknij przeglądarkę
driver.quit()
'''
# Add base path to all links
def add_base_path(website_link, list_links):
    list_links_with_base_path = []

    for link in list_links:

        if not link.startswith('/'):
            link_with_base_path = website_link + link
            list_links_with_base_path.append(link_with_base_path)

  # if link.startswith('https://') dont add base path
        elif link.startswith('http://'):
            list_links_with_base_path.append(link)

        elif link.startswith('.'):
            link_with_base_path = website_link + link.split('/')[-1]
            list_links_with_base_path.append(link_with_base_path)

    return list_links_with_base_path

link_list = add_base_path('https://python.langchain.com/en/latest/', sub_links)
link_list_print = print(link_list)



def save_content(link_list):
    for i, link in enumerate(link_list):
        html_data = get_data(link)
        soup = BeautifulSoup(html_data, "html.parser")
        text = soup.get_text()

        # Remove the first 835 lines
        lines = text.splitlines()
        cleaned_text = "\n".join(lines[835:])

        # Get the first 3 words in the cleaned text
        words = cleaned_text.split()[:3]
        file_name_prefix = "_".join(words)

        # Replace special characters and spaces with an underscore
        file_name_prefix = re.sub(r"[^a-zA-Z0-9]+", "_", file_name_prefix)

        # Get the current working directory
        current_dir = os.getcwd()

        # Move up one level to the parent directory
        parent_dir = os.path.dirname(current_dir)

        # Set the path to the data folder
        data_folder = os.path.join(parent_dir, "/home/vboxuser/PycharmProjects/AI/vector-search1/scrapper/scraped-data-from-url-pages")

        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        # Set the path to the output file
        output_file = os.path.join(data_folder, f"{i}_{file_name_prefix}.txt")

        # Save the cleaned content to the output file
        with open(output_file, "w") as f:
            f.write(cleaned_text)


# Save the content of the links into txt files
save_content(link_list)'''