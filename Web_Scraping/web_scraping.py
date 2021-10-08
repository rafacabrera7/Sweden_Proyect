from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://arbetsformedlingen.se/platsbanken/annonser?p=5:tPox_ie4_X9X&l=2:CifL_Rzy_Mku').text
soup = BeautifulSoup(html_text, 'lxml')
# print(soup)
jobs = soup.find('div', class_='card-container')
print(jobs)
