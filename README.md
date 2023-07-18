# web_scraper_py
# URL Extractor

## Overview
This is a Python tool that extracts URLs recursively from either of www.curlie.org or www.wikipedia.org, including sub-pages. The tool uses the BeautifulSoup library to parse the HTML content of the web pages and extract all links and sub-pages. The extracted URLs are stored in a set to eliminate duplicates.

## Usage
To use the tool, simply run the `web_scraper.py` script and specify the URL of the webpage you want to extract URLs from as a command-line argument. For example:

python web_scraper.py URL depth
```
python web_scraper.py https://curlie.org 1
```

The tool will then recursively extract URLs from the specified webpage and all sub-pages, and print them to the console.

## Requirements
The tool requires Python 3 and the BeautifulSoup library to be installed. You can install the BeautifulSoup library using pip:

```
pip install beautifulsoup4
```

## Future work
There are several ways in which the tool could be improved, such as adding support for more websites, filtering out irrelevant URLs, and implementing error handling for cases where a webpage cannot be accessed or parsed. Additionally, the tool could be extended to support more advanced features, such as extracting metadata from web pages or analyzing the content of extracted URLs.
