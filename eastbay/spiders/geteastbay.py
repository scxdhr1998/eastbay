import re

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

            #获取网页路径
            item['url'] = 'https://www.eastbay.com/'+goods_list.find('a')['href']
            request = scrapy.Request(url='https://www.eastbay.com/'+goods_list.find('a')['href'],callback=self.details,meta={'item':item})

            yield request


    def details(self,response):

        item = response.meta['item']
        content = response.body
        soup = bs4.BeautifulSoup(content, "html.parser")

        #获取价格
        item['price'] = soup.find('span', attrs={'ProductPrice-final'}).text

        #获取尺寸
        list = soup.find_all('div',attrs='c-form-field c-form-field--radio ProductSize')
        size =''
        for list in list:
            size = size + ',' + list.find('span', attrs={'c-form-label-content'}).text
        item['size'] = size[1:]

        #获取标题
        item['title'] = soup.find('span',attrs='ProductName-primary').text

        #获取颜色
        item['color'] = soup.find('p',attrs='ProductDetails-form__label').text

        # 获取图片路径
        img_url = response.xpath("//span[@class='c-image product c-image--square']").extract()
        img_url = str(img_url)
        img_urls = re.findall(r'\bhttps\S*?alpha\b',img_url)
        item['img_urls'] = img_urls

        #获取细节描述
        item['details'] = soup.find('div',attrs='ProductDetails-description').text.replace('<br>','').replace('<br/>','').replace('<strong>','').replace('</strong>','')







        yield item



