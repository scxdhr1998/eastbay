# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EastbayItem(scrapy.Item):
     title = scrapy.Field()
     img_urls = scrapy.Field()
     price = scrapy.Field()
     size = scrapy.Field()
     color = scrapy.Field()
     details = scrapy.Field()
