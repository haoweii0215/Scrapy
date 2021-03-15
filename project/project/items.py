import scrapy

class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    log = scrapy.Field()
    createdtime = scrapy.Field()
