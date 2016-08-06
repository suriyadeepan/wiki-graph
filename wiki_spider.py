import scrapy
from bs4 import BeautifulSoup
import requests

_BASE_URL = 'https://en.wikipedia.org'

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/Rio_de_Janeiro']

    def parse(self,response):
        title = response.xpath('//h1[contains(@class,"firstHeading")]/text()').extract_first()
        soup = BeautifulSoup(response,'lxml')
        urls = []
        titles = []
        for url_tag in response.xpath("//a"):
            href = url_tag.xpath("@href").extract_first()
            if href.startswith('/wiki/') and not 'File' in href:
                urls.append(_BASE_URL + href)
                titles.append(url_tag.xpath('@title').extract_first())
                
        self_url = response.url
        
        for url,ext_title in zip(urls,titles):
            yield { 'title' : title, 'self_url' : self_url, 'ext_url' : url , 'ext_title' : ext_title}
            yield scrapy.Request(url, callback=self.parse)
