import random

from scrapy import signals
from eastbay.settings import IPPOOL


class MyproxiesSpiderMiddleware(object):

    def __init__(self, ip=''):
        self.ip = ip

    # 配置代理
    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip["ipaddr"])
        request.meta["proxy"] = "http://" + thisip["ipaddr"] # https代理