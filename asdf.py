from bs4 import BeautifulSoup
import requests

with open('simple.htm') as html_file:
    soup = BeautifulSoup (html_file,'lxml')