import requests
from bs4 import BeautifulSoup
import cv2 as cv

url = "https://www.imdb.com/name/nm0424060/mediaindex?ref_=nm_phs_md_sm"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

for image in images:
    url = image["src"]
    print(url)
    r = requests.get(url)
    with open('./image/{}'.format(url.split('/')[-1]), 'wb') as f:
        f.write(r.content)
