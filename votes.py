#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv > 1):
    name = sys.argv[1]
else:
    print("No package name provided")
    sys.exit()

url = f'https://aur.archlinux.org/packages/{name}'  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


tags = soup.find_all(['th', 'td'])
data = [tag.get_text(strip=True) for tag in tags]

for i in range(len(data)):
    if (data[i] == "Votes:"):
        print(f'AUR votes for "{name}": ' + data[i + 1])
        sys.exit()
print(f'No package found with name: "{name}"')
