import scrapy
from scrapy.http import Request
import bs4
from ..items import EastbayItem

class GeteastbaySpider(scrapy.Spider):

    name = 'geteastbay'

    allowed_domains = ['www.eastbay.com']

    start_urls = ['https://www.eastbay.com/category/sale.html?query=sale%3Arelevance%3AstyleDiscountPercent%3ASALE%3Agender%3AMen%27s%3Abrand%3AASICS+Tiger']
    #一级爬虫
    def parse(self, response):

        item = EastbayItem()

        content = response.body

        soup = bs4.BeautifulSoup(content, "html.parser")

        goods_list = soup.find_all('li',attrs={'product-container col'})
        #获取二级页面路径赋值给item
        for goods_list in goods_list:
            #url_list.append('https://www.eastbay.com/'+goods_list.find('a')['href'])

            item['url'] = 'https://www.eastbay.com/'+goods_list.find('a')['href']

            yield item
    #         yield scrapy.Request(url='https://www.eastbay.com/'+goods_list.find('a')['href'],callback=self.details,meta={'item':item})
    #
    # def details(self,response):
    #
    #     item = response.meta['item']
    #
    #     content_list = response.xpath('//span[@class="ProductPrice-final"]/text()')
    #
    #     print(content_list)


