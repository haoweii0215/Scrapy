import pandas as pd
import json
from datetime import date, timedelta, datetime
import numpy as np
from project.items import ProjectItem
import scrapy

class Project(scrapy.Spider):
    name = 'Project'
    start_urls = ['Your_URL&pagenums=1']

    def parse(self, response):
        data = json.loads(response.text)
        stop = data['pages'] # get total page numbers
        for i in range(1, stop+1):
            q_url = f'Your_URL&pagenums={i}'
            yield scrapy.Request(url=q_url, callback=self.parse_data_process)

    def parse_data_process(self,response):
        item = ProjectItem()
        item['date'] = date.today().strftime('%Y-%m-%d')
        item['log'] = response.text
        item['createdtime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return item