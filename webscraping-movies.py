from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font






webpage = 'https://www.boxofficemojo.com/year/2024/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
rank = ''
Release = ''
Gross = ''
Release_date = ''
number_of_theaters = 0
average_per_theater = 0

table_rows = soup.findAll('tr')



for rows in table_rows[1:6]:
    td = rows.findAll('td')
    movie_rank = td[0].text
    movie_release = td[1].text
    movie_gross = int(td[5].text.replace(',', '').replace('$',''))
    movie_date =td[8].text
    movie_theaters = int(td[6].text.replace(',',''))

    
    average_per_theater = round(movie_gross/movie_theaters)

    print(movie_rank)
    print(movie_release)
    print(movie_date)
    print(movie_theaters)
    print(movie_gross)
    print(average_per_theater)
    print()
    print()




