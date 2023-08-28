import scrapy


class PubgspidySpider(scrapy.Spider):
    name = "pubgspidy"
    allowed_domains = ["steamcharts.com"]
    start_urls = ["https://steamcharts.com/app/578080#All"]

    def parse(self, response):
        yield {
            "Month" : [ item.replace("\n\t\t\t\t","").replace("\n\t\t\t\t\t") for item in response.css("td.month-cell ::text").get() ],
            "Avg_Players" : response.css("td.num-f ::text").getall()
            
        }