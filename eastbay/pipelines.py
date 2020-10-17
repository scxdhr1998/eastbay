import json,codecs

class JsonPipelines(object):
    def __init__(self):
        self.file = open('spiderdata.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.file.close()