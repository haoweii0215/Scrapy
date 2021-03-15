# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from project import settings
from project.items import ProjectItem

class ProjectPipeline:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host = settings.MYSQL_HOST,
        user = settings.MYSQL_USER,
        passwd = settings.MYSQL_PASS,
        database = settings.MYSQL_DB
    )
        self.mycursor = self.mydb.cursor()
    def process_item(self, item, spider):
        if item.__class__ == ProjectItem:
            sql = """INSERT INTO Your_Database VALUES(%s,%s,%s)"""
            self.mycursor.execute(sql, (item['date'], item['log'], item['createdtime']))
            self.mydb.commit()
            self.mydb.close()
        return item
