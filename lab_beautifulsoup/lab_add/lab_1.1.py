from bs4 import BeautifulSoup
import requests

URL = "https://weather.naver.com/air/airFcast.nhn"  #미세먼지 
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')

airTable = soup.find_all("div", class_="list_air_inn")

for air in airTable:
    today = air.find_all("li")
    for data in today:
        print(data.text)