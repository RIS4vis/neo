import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()

    def crawl(self, url):
        if url not in self.visited:
            print(f'Crawling: {url}')
            self.visited.add(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            self.extract_data(soup)
            for link in soup.find_all('a', href=True):
                full_url = requests.compat.urljoin(url, link['href'])
                self.crawl(full_url)

    def extract_data(self, soup):
        # Sample data extraction
        for item in soup.find_all('h1'):
            print(f'Found heading: {item.get_text()}')

if __name__ == '__main__':
    crawler = WebCrawler('http://example.com')
    crawler.crawl(crawler.base_url)