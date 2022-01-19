#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup##this does not work. It is borked

def parse_rom_urls():
  # URLS
  rooturl = "https://archive.org/download/nointro.n64/"

  soup = BeautifulSoup(requests.get(rooturl).text, 'html.parser')

  links = [rooturl + a.get('href') for a in soup.find_all('a', href=True)]

  return([link for link in links if link.endswith(".7z")])

if __name__ == '__main__':
  print(parse_rom_urls())