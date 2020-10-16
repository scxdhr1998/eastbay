import requests        #导入requests包
url = 'https://www.baidu.com/s?wd=爬虫&pn=0'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)