# Marvish Chandra

import requests
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/id/Ridarak'

response = requests.get(url)

soup = BeautifulSoup(response.text,features='html.parser')
steam_name_tag = soup.find('span',{'class': 'actual_persona_name'}).text
profile_location = soup.find('div',{'class': 'header_real_name'}).text
profile_description = soup.find('div',{'class':'profile_summary'}).text
print(steam_name_tag)
print(profile_location)
print(profile_description)
