## Week 12: Web Scraping Basics

- Introduction to web scraping
- Popular Python libraries for scraping (e.g., BeautifulSoup, Scrapy)
- Fetching and parsing HTML content
- Extracting data from websites
- Ethical considerations and best practices
- Practical exercises and assignments

### What is Web Scraping?

Web scraping is the process of extracting data from websites. It involves fetching the HTML content of a web page and parsing it to extract the desired information. Web scraping can be used to collect data from various sources on the internet, such as news articles, product listings, weather forecasts, and more.

### Why Use Web Scraping?

Web scraping allows you to automate the process of collecting data from websites, saving you time and effort. It can be used for a variety of purposes, such as:

- **Data collection**: Scraping data from multiple websites to create a dataset for analysis or research.

- **Competitive analysis**: Monitoring competitors' websites to gather information on their products, pricing, and promotions.

- **Content aggregation**: Collecting news articles, blog posts, or other content from different sources to create a curated feed.

- **Lead generation**: Extracting contact information from websites to generate leads for marketing campaigns.

- **Market research**: Gathering data on consumer trends, product reviews, and other market insights from online sources.

### Popular Python Libraries for Web Scraping

Python provides several libraries for web scraping, each with its own features and capabilities. Some of the most popular libraries for web scraping in Python include:

- **Beautiful Soup**: A Python library for parsing HTML and XML documents. It provides a simple interface for navigating and searching the document tree, making it easy to extract data from web pages.

- **Scrapy**: An open-source web crawling and scraping framework written in Python. It provides a powerful set of tools for extracting data from websites, handling requests, and processing responses.

- **Requests**: A Python library for making HTTP requests. It allows you to send GET and POST requests to web servers, retrieve web pages, and interact with web APIs.

- **Selenium**: A web automation tool that can be used for web scraping. It allows you to interact with web pages, fill out forms, and simulate user actions in a browser.

### Fetching and Parsing HTML Content

To scrape data from a website, you first need to fetch the HTML content of the web page. This can be done using the `requests` library in Python, which allows you to send HTTP requests to web servers and retrieve web pages.

Once you have fetched the HTML content, you can parse it using a library like Beautiful Soup to extract the desired information. Beautiful Soup provides functions for navigating the HTML document tree, searching for specific elements, and extracting data based on tags, attributes, and text content.

```python

import requests

from bs4 import BeautifulSoup

# Fetch the HTML content of a web page

url = 'https://example.com'

response = requests.get(url)

html_content = response.text

# Parse the HTML content using Beautiful Soup

soup = BeautifulSoup(html_content, 'html.parser')

# Extract data from the web page

title = soup.title.text

print(title)

```

In this example, we use the `requests` library to fetch the HTML content of a web page and the `BeautifulSoup` library to parse the content. We extract the title of the web page and print it to the console.

### Extracting Data from Websites

Once you have fetched and parsed the HTML content of a web page, you can extract the desired data by searching for specific elements, attributes, or text content. Beautiful Soup provides functions for finding elements by tag name, class name, ID, and other attributes.

```python

# Find all links on the web page

links = soup.find_all('a')

for link in links:

    print(link.get('href'))

# Find all paragraphs with a specific class

paragraphs = soup.find_all('p', class_='content')

for paragraph in paragraphs:

    print(paragraph.text)

```

In this example, we use the `find_all` method of Beautiful Soup to search for all links (`<a>` tags) and paragraphs (`<p>` tags) on the web page. We then extract the `href` attribute of each link and the text content of each paragraph.

### Ethical Considerations and Best Practices

When scraping data from websites, it's important to follow ethical guidelines and best practices to avoid legal issues and respect the rights of website owners. Some key considerations include:

- **Respect robots.txt**: Check the `robots.txt` file of a website to see if web scraping is allowed or restricted. Avoid scraping pages that are marked as disallowed in the `robots.txt` file.

- **Use proper headers**: Set the `User-Agent` header in your HTTP requests to identify your web scraping bot and provide contact information in case of issues.

- **Avoid overloading servers**: Limit the frequency and volume of your requests to avoid overloading the web server and causing disruptions.

- **Respect terms of service**: Review the terms of service of a website to ensure that your web scraping activities comply with their guidelines.

- **Observe copyright laws**: Respect the intellectual property rights of website owners and avoid scraping copyrighted content without permission.

By following these guidelines and best practices, you can conduct web scraping activities responsibly and ethically.

### Practical Exercises

1. Write a Python program that scrapes the latest news headlines from a news website and displays them in a formatted list.

2. Write a Python program that scrapes product listings from an e-commerce website and saves them to a CSV file.

3. Write a Python program that scrapes weather forecast data from a weather website and displays it in a user-friendly format.
