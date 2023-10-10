import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

f = open("Links1.txt", "w")

urls = []
for link in soup.find_all('a'):
    data = link.get('href')
    f.write(data)
    f.write("\n")

f.close()