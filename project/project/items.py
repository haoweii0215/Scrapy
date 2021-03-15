import scrapy

class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    log = scrapy.Field()
    createdtime = scrapy.Field()