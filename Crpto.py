from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://cryptorank.io/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers = headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

table_rows = soup.findAll('tr')

for row in table_rows[1:6]:
    td = row.findAll('td')
    name = td[2].text
    price = float(td[3].text.replace('$', '').replace(',', ''))
    change = round(float(td[4].text.replace('%', ''))/100,4)


    corresponding_price = round(price * (1+change),2)

    print(f'Name of currency: {name}  Closing price: {price}  Daily change: {change}  Corresponding_price: {corresponding_price}')