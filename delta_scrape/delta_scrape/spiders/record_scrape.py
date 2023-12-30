import scrapy


class RecordScrapeSpider(scrapy.Spider):
    name = "record_scrape"
    allowed_domains = ["www.deltacomputersystems.com"]
    start_urls = ["https://www.deltacomputersystems.com/cgi-bpa3/BPMCGI02?HTMCNTY=AL05&HTMBASE=C&HTMKEY=0000133073&"]

    def parse(self, response):
        all_pre=response.css("pre::text")
        self.log('\n'.join(all_pre.getall()))
        
