import scrapy


class TableScrapeSpider(scrapy.Spider):
    name = "table_scrape"
    allowed_domains = ["www.deltacomputersystems.com"]
    start_urls = ["https://www.deltacomputersystems.com/cgi-bpa3/BPMCGI03?HTMCNTY=AL05&HTMBASE=C&HTMSEARCH=BEGIN&HTMWILDNAME=&HTMNAME=&HTMPROPERTYADDR=&HTMBUILDING=&HTMCONTRACTOR=&HTMPARCEL1=&HTMPARCEL2=&HTMPARCEL3=&HTMPARCEL4=&HTMPARCEL5=&HTMPARCEL6=&HTMPARCEL7=&HTMPARCEL8=&HTMPPIN=&HTMPERMIT=133060&HTMSUBMIT=Submit"]

    # def start_requests(self):

    #     return ['https://www.deltacomputersystems.com/cgi-bpa3/BPMCGI03?HTMCNTY=AL05&HTMBASE=C&HTMSEARCH=BEGIN&HTMWILDNAME=&HTMNAME=&HTMPROPERTYADDR=&HTMBUILDING=&HTMCONTRACTOR=&HTMPARCEL1=&HTMPARCEL2=&HTMPARCEL3=&HTMPARCEL4=&HTMPARCEL5=&HTMPARCEL6=&HTMPARCEL7=&HTMPARCEL8=&HTMPPIN=&HTMPERMIT=133060&HTMSUBMIT=Submit']
      
# PERMIT	BUILDING PERMIT	NAME	NAME TYPE	PROPERTY ADDRESS	PPIN  	PARCEL 	ZONING DISTRICT
    def parse(self, response):
        all_rows=response.css("tr")
        for row in all_rows:
            # self.log(type(row))
            # self.log(row.attrib)
            # #C8D3DE'
            if 'bgcolor' in row.attrib and row.attrib['bgcolor'] in ['#C8D3DE','#FFFFFF' ]:

                columns=row.css('td')
                self.log(columns)
                for column in columns:
                    self.log(column.xpath('string(.)').get().strip())
                    
                # pass
                # self.log(row)
        # self.log(response.url)
        # yield {
        #     'rows': response.css('tr[bgcolor="#FFFFFF"]').getall()
        # }