# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:47:50 2020

@author: Kapil
"""


from bs4 import BeautifulSoup
import requests
url = 'https://surat.craigslist.org/d/general-community/search/com'
response = requests.get(url)