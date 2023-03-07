import requests
import csv
from bs4 import BeautifulSoup
from time import sleep 
import os
import selenium import webdriver




# Set the URL to scrape
driver = webdriver.Chrome()
url = 'https://www.kayak.com/flights?from=Europe&sort=bestflight_a&fs=stops=0'

# Send a GET request to the URL and get the page HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the flight search results
results = soup.find_all('div', {'class': 'Flights-Results-FlightResultItem'})

# Create a list to hold the flight data
flight_data = []

# Loop through the flight search results and extract the data we want
for result in results:
    airline = result.find('span', {'class': 'section-times-airline'}).text.strip()
    flight_num = result.find('span', {'class': 'section-times-flight-num'}).text.strip()
    duration = result.find('span', {'class': 'section-times-duration'}).text.strip()
    price = result.find('a', {'class': 'booking-link'})['data-price']
    origin = result.find('div', {'class': 'section-route airports inline-block'}).find_all('span')[0].text.strip()
    destination = result.find('div', {'class': 'section-route airports inline-block'}).find_all('span')[1].text.strip()
    flight_data.append([airline, flight_num, duration, price, origin, destination])

# Write the flight data to a CSV file
with open('flight_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Airline', 'Flight Number', 'Duration', 'Price', 'Origin', 'Destination'])
    for data in flight_data:
        writer.writerow(data)

print('Flight data saved to flight_data.csv')

url = 'https://www.kayak.com/flights?from=Europe&sort=bestflight_a&fs=stops=0'

# Send a GET request to the URL and get the page HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the flight search results
results = soup.find_all('div', {'class': 'Flights-Results-FlightResultItem'})

# Create a list to hold the flight data
flight_data = []

# Loop through the flight search results and extract the data we want
for result in results:
    airline = result.find('span', {'class': 'section-times-airline'}).text.strip()
    flight_num = result.find('span', {'class': 'section-times-flight-num'}).text.strip()
    duration = result.find('span', {'class': 'section-times-duration'}).text.strip()
    price = result.find('a', {'class': 'booking-link'})['data-price']
    origin = result.find('div', {'class': 'section-route airports inline-block'}).find_all('span')[0].text.strip()
    destination = result.find('div', {'class': 'section-route airports inline-block'}).find_all('span')[1].text.strip()
    flight_data.append([airline, flight_num, duration, price, origin, destination])

# Write the flight data to a CSV file
with open('flight_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Airline', 'Flight Number', 'Duration', 'Price', 'Origin', 'Destination'])
    for data in flight_data:
        writer.writerow(data)

print('Flight data saved to flight_data.csv')

url = 'https://www.kayak.com/flights?from=Europe&sort=bestflight_a&fs=stops=0'

# Send a GET request to the URL and get the page HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the flight search results
results = soup.find_all('div', {'class': 'Flights-Results-FlightResultItem'})

# Create a list to hold the flight data
flight_data = []

# Loop through the flight search results and extract the data we want
for result in results:
    airline = result.find('span', {'class': 'section-times-airline'}).text.strip()
    flight_num = result.find('span', {'class': 'section-times-flight-num'}).text.strip()
    duration = result.find('span', {'class': 'section-times-duration'}).text.strip()
    price = result.find('a', {'class': 'booking-link'})['data-price']
    origin = result.find('div', {'class': 'section-route airports inline-block'}).find_all('span')[0].text.strip()
    destination = result.find('div', {'class': 'section-route airports inline-block'}).find_all('span')[1].text.strip()
    flight_data.append([airline, flight_num, duration, price, origin, destination])

# Write the flight data to a CSV file
with open('flight_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Airline', 'Flight Number', 'Duration', 'Price', 'Origin', 'Destination'])
    for data in flight_data:
        writer.writerow(data)

print('Flight data saved to flight_data.csv')
