Hacker News Scraper

A small learning project built while studying web scraping with Python. This script scrapes news articles from Hacker News, filters them by a minimum number of points, and sorts them from highest to lowest score.

Usage

Run the script from your terminal and specify the number of pages to scrape and the minimum number of votes:

python3 scraper.py <count_of_pages> <minimum_votes>

For example:

python3 scraper.py 5 150

This will scrape 5 pages of Hacker News and display only articles with at least 150 points, sorted by popularity.