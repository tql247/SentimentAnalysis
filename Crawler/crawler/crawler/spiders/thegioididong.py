from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
# from scrapy.selector import HtmlXPathSelector
from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com",
    ]

    def parse(self, response):
        categories = Selector(response).xpath("//div[@class='wrap-nav']/nav/a/@href")

        for category in categories:
            
            category = response.urljoin(category.extract())
            yield Request(category, callback = self.parse_category)

    
    def parse_category(self, response):
        try:
            items = Selector(response).xpath("//ul[contains(@class, 'homeproduct') and contains(@class, 'item2020')]/li/a/@href").extract()

            for item in items:
                item += '/danh-gia'
                item = response.urljoin(item)
                yield Request(item, callback= self.parse_item)
        except:
            print('error')


    def parse_item(self, response):
        fields = Selector(response).xpath("//div[@class='rc']/p")

        for comment in fields:
            item = CrawlerItem()
            print(comment)

            item['Comment'] = comment.xpath("./i/text()").extract()
            item['Rating'] = str(len(comment.xpath(".//i[@class='iconcom-txtstar']"))) + '/5'

            yield item

