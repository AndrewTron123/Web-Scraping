import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapter = random.randint(1,21)
if chapter < 10:
    chapter = '0' + str(chapter)
else:
    chapter = str(chapter)
webpage = 'https://ebible.org/asv/JHN' + chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('div', class_= 'p')

myverses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split('.')

    for v in verse_list:
        myverses.append(v)


mychoice = random.choice(myverses)

print(f"Chapter: {chapter} Verse: {mychoice}")















'''
verse_number = random.randint(0, len(page_verses)-1)  


random_verse = page_verses[verse_number]

print(random_verse.text)
'''