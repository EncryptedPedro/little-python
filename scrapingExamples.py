
#BeautifulSoup
from bs4 import BeautifulSoup
import requests
import pandas as pd
URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#print(soup)

#Scrapy
#import scrapy
#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {'quote': quote.css('span.text::text').get()}


#Selenium
#from selenium import webdriver
#driver = webdriver.Firefox()
#driver.get("http://www.example.com")


#ParseHub is easy scraping tool

#using pandas (stricly tabular data, beautifulSoup is still the standard)
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
data = pd.read_html(URL)
#print(data)

df = data[2]
print(df)