import requests
from bs4 import BeautifulSoup
import pprint
import sys

if len(sys.argv) != 3:
    print("Usage: python scraper.py <count_of_pages> <minimum_votes>")
    sys.exit()
try:
    pages = int(sys.argv[1])
    minimum_votes = int(sys.argv[2])

    if pages < 1 or minimum_votes < 0:
        raise ValueError

except ValueError:
    print("Please enter valid numbers.")
    sys.exit()


mega_links = []
mega_subtext = []


try:
    for page in range(1, pages + 1):
        url = f'https://news.ycombinator.com/news?p={page}'
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        mega_links.extend(soup.select('.titleline'))
        mega_subtext.extend(soup.select('.subtext'))

except requests.exceptions.RequestException as error:
    print(f"Request error: {error}")
    sys.exit()


def sort_stories(hnlink):
    return sorted(hnlink, key= lambda k: k['vote'], reverse=True)

def custom_news(links, subtext, needed_point):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.select_one('a').get('href', None)
        vote = subtext[idx].select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points >= needed_point:
                hn.append({'title':title, 'link':href, 'vote':points})
    return sort_stories(hn)


articles = custom_news(mega_links, mega_subtext, minimum_votes)

pprint.pprint(articles)

needed_articles_count = len(articles)
print(f"{needed_articles_count} articles have been found")
