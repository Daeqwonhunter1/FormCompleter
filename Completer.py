import urllib3
from bs4 import BeautifulSoup



http = urllib3.PoolManager()
response = http.request('GET', "http://wwwsearch.sourceforge.net/ClientForm/example.html").data
soup = BeautifulSoup(response, 'html.parser')

print(soup.prettify())