import scrapy
from bs4 import BeautifulSoup
import requests

_BASE_URL = 'https://en.wikipedia.org'

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/Transhumanism']

    def parse(self,response):
        self_title = response.xpath('//h1[contains(@class,"firstHeading")]/text()').extract_first()
        self_url = response.url
        soup = BeautifulSoup(response.body,'lxml')
        # focus on links from paragraphs
        link_tags = []
        for p in soup.findAll('p'):
            link_tags.extend(p.findAll('a'))
        # find all the external links and corresponding titles
        ext_links  = []
        ext_titles = []
        for tag in link_tags:
            if not any( x in str(tag) for x in ['cite_note','File']):
                if 'title' in tag.attrs and 'href' in tag.attrs:
                    ext_titles.append(tag['title'])
                    ext_links.append(_BASE_URL + tag['href'])
        
        for ext_link, ext_title in zip(ext_links,ext_titles):
            yield { 'title' : self_title, 'self_url' : self_url, 'ext_url' : ext_link , 'ext_title' : ext_title}
            yield scrapy.Request(ext_link, callback=self.parse)
