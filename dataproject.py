# question: How times in the 100 year span from 1915 to 2015 has there been a white Christmas?
# import csv and requests modules
import csv
import requests

# set up URL for request
endpoint = 'https://api.darksky.net/forecast/'
api_key = 'da5d52438b53e27259e8e2bdc2f7c51f'
lat = '40.7128'
lon= '74.0059'
year = 2000 # int(input("Choose year? "))
time = '%d-12-25T00:00:00' % year

# url for request
url = endpoint + api_key + '/' + lat + ',' + lon + ',' + time

# make request
r = requests.get(url)

weather = r.json()
print(weather['daily']['data'][0]['precipType'])

# open file in write mode
csvfile= open('dataproject.csv', 'w')

# create the csv writer
csvwriter= csv.writer(csvfile, delimiter= ',')

    