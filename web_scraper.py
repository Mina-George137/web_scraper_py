import requests
from bs4 import BeautifulSoup
import sys


def extract_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    links = []
    for a in soup.find_all("a", href=True):
        link = a["href"]
        if link is not None:
            if link and not link.startswith("#"):
                if "http" in link:
                    links.append(link)
                else:
                    links.append(f"{url}/{link}")

    return links


def extract_all_urls(url, depth):
    d = depth - 1
    links = extract_urls(url)
    print(depth)
    print(d)
    print(len(links))
    print(links)
    visited = []
    for link in links:
        if d >= 0 and link != '' and link not in visited:
            visited.append(link)
            new_links = extract_all_urls(link, d)
            links += new_links
    return links


if __name__ == "__main__":
    url = sys.argv[1]
    depth = int(sys.argv[2])
    urls = extract_all_urls(url, depth)
