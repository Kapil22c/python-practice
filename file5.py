import pandas as pd
import requests
from bs4 import BeautifulSoup

print(pd.__version__)
#Web scrapping with python

#Use libraries like beautiful soup and requests

# one essential skill that every developer needs


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.Xn8K5ogzbIU')
soup = BeautifulSoup(page.content, 'html.parser')  #Will return whole source d=code of the given link


week=soup.find(id="seven-day-forecast-body")
 #print(week)

items=week.find_all(class_='tombstone-container')
#print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names= [item.find(class_='period-name').get_text() for item in items]
print(period_names)

short_description=[item.find(class_='short-desc').get_text() for item in items]
print(short_description)

temperatures=[item.find(class_='temp').get_text() for item in items]
print(temperatures)


weather_stuff= pd.DataFrame(
    {
        'period': period_names,
        'short_description': short_description,
        'temperatures': temperatures,
    })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
