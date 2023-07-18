from bs4 import BeautifulSoup
import requests
import re
import os


class WebsiteScraper:
    def __init__(self):
        self.website_url = None
        self.sub_links = []
        self.link_list = []

    def get_data(self, url):
        r = requests.get(url)
        return r.text

    def get_links(self, website_link):
        html_data = self.get_data(website_link)
        soup = BeautifulSoup(html_data, "html.parser")
        list_links = []
        for link in soup.find_all("a", href=True):
            list_links.append(link["href"])
        return list_links

    def add_base_path(self, website_link, list_links):
        list_links_with_base_path = []
        for link in list_links:
            if not link.startswith('/'):
                link_with_base_path = website_link + link
                list_links_with_base_path.append(link_with_base_path)
            elif link.startswith('http://'):
                list_links_with_base_path.append(link)
            elif link.startswith('.'):
                link_with_base_path = website_link + link.split('/')[-1]
                list_links_with_base_path.append(link_with_base_path)
        return list_links_with_base_path

    def save_content(self, link_list):
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
            data_folder = os.path.join(parent_dir, "/Langchain_Ask_App/scrapper/scraped-data-from-url-pages")

            # Create the data folder if it doesn't exist
            if not os.path.exists(data_folder):
                os.makedirs(data_folder)

    def run(self):
        self.website_url = input("Enter the website URL (e.g., https://python.langchain.com/en/latest/index.html): ")

        if not self.website_url.startswith('https://'):
            self.website_url = 'https://' + self.website_url

        try:
            requests.get(self.website_url)
        except requests.exceptions.RequestException:
            print("Invalid website URL. Please try again.")
            return

        self.sub_links = self.get_links(self.website_url)
        self.link_list = self.add_base_path(self.website_url, self.sub_links)
        self.save_content(self.link_list)


scraper = WebsiteScraper()
scraper.run()
