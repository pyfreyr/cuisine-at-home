# -*- coding: utf-8 -*-
import scrapy


class RecipeSpider(scrapy.Spider):
    name = 'recipe'
    allowed_domains = ['meishij.net']
    start_urls = ['http://meishij.com/']

    def parse(self, response):
        pass
