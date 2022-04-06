from bs4 import BeautifulSoup
import bs4
import requests
import re

website = 'https://xkcd.com'
response = requests.get(website)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
        print("Didn't match with the URL: {}".format(url))
        continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(website, url)
        response = requests.get(url)
        f.write(response.content)
