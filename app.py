# We import requests and BeautifulSoup to scrape addresses from Buc-ee's website
# To collect data from Google Maps API we import googlemaps
import googlemaps
# For data manipulation and analysis we import pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
# We don't want our API key to be public, so we use dotenv to load it from a .env file
from dotenv import load_dotenv
# To display data in a table we import itables
from itables import show

load_dotenv()

buc_ees_list = []

def getSoup(url):
    page = requests.get(url) 
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

soup = getSoup('https://www.buc-ees.com/locations/')

# Find all the divs with the class 'bucees-location'
locations = soup.find_all('div', class_='bucees-location')

# Print each of the locations
for location in locations:
    
    # Find the address. It is in a div with the class 'bucees-location-address'. Don't recurse.
    address = location.find('div', class_='bucees-location-address', recursive=False)

    buc_ees_list.append(
        {
            'name': location.find('h4').text,
            'address': address.text,
        }
    )

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(buc_ees_list)

# Display the DataFrame
print(df)