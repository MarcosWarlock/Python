#!/usr/bin/env python3.5
#
# MarcosWarlock
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

url = 'http://www.esa.institucional.ws/site/ProvasAnteriores.aspx'
resp = urlopen(url).read()
soup = BeautifulSoup(resp, 'html.parser')

for link in soup.find_all('a'):
    if link.get('href')[-3:] in "pdf":
        f = urlopen(link.get('href'))
        nome = str(link.get('href').split('/')[-1])
        
        with open(nome, 'wb') as file:
            file.write(f.read())
            print(nome + ' --> ' + str(os.getcwd()))
    else:
        continue


