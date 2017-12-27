import requests
from bs4 import BeautifulSoup

# scrape kõik pealkirjad antud urlist
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html5lib")

# kasutaja sisestab failinime
filename = input("Sisesta failinimi: ")

# kirjutab kõik need pealkirjad faili, mille nime kasutaja sisestas
with open(filename, 'w', encoding="utf8") as f:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            f.write(story_heading.a.text.replace("\n", " ").strip())
        else:
            f.write(story_heading.contents[0].strip())

