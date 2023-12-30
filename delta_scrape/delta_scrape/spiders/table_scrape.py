import scrapy


class TableScrapeSpider(scrapy.Spider):
    name = "table_scrape"
    allowed_domains = ["www.deltacomputersystems.com"]
    # start_urls = ["https://www.deltacomputersystems.com/cgi-bpa3/BPMCGI03?HTMCNTY=AL05&HTMBASE=C&HTMSEARCH=BEGIN&HTMWILDNAME=&HTMNAME=&HTMPROPERTYADDR=&HTMBUILDING=&HTMCONTRACTOR=&HTMPARCEL1=&HTMPARCEL2=&HTMPARCEL3=&HTMPARCEL4=&HTMPARCEL5=&HTMPARCEL6=&HTMPARCEL7=&HTMPARCEL8=&HTMPPIN=&HTMPERMIT=133060&HTMSUBMIT=Submit"]

    def start_requests(self):
        # uncomment to get permits below stated number
        # current_permit = 133501
        current_permit = 50000001 	 
        # uncomment to get lower number values
        # while current_permit > 0:
        while current_permit < 50004235:
            url = f'https://www.deltacomputersystems.com/cgi-bpa3/BPMCGI03?HTMCNTY=AL05&HTMBASE=C&HTMSEARCH=BEGIN&HTMWILDNAME=&HTMNAME=&HTMPROPERTYADDR=&HTMBUILDING=&HTMCONTRACTOR=&HTMPARCEL1=&HTMPARCEL2=&HTMPARCEL3=&HTMPARCEL4=&HTMPARCEL5=&HTMPARCEL6=&HTMPARCEL7=&HTMPARCEL8=&HTMPPIN=&HTMPERMIT={current_permit}&HTMSUBMIT=Submit'
            current_permit+=500
            yield scrapy.Request(url=url, callback=self.parse)
        # return ['https://www.deltacomputersystems.com/cgi-bpa3/BPMCGI03?HTMCNTY=AL05&HTMBASE=C&HTMSEARCH=BEGIN&HTMWILDNAME=&HTMNAME=&HTMPROPERTYADDR=&HTMBUILDING=&HTMCONTRACTOR=&HTMPARCEL1=&HTMPARCEL2=&HTMPARCEL3=&HTMPARCEL4=&HTMPARCEL5=&HTMPARCEL6=&HTMPARCEL7=&HTMPARCEL8=&HTMPPIN=&HTMPERMIT=133060&HTMSUBMIT=Submit']
      
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
                list_of_values=[]
                for column in columns:
                    list_of_values.append(column.xpath('string(.)').get().strip())

                self.log(list_of_values)
                # uncomment to get lower values and indent yield 
                # if int(list_of_values[0]) < 50000001:
	 
                yield {
                    'PERMIT': list_of_values[0],
                    'BUILDING PERMIT': list_of_values[1],
                    'NAME': list_of_values[2],
                    'NAME TYPE': list_of_values[3],
                    'PROPERTY ADDRESS': list_of_values[4],
                    'PPIN' : list_of_values[5],
                    'PARCEL': list_of_values[6],
                    'ZONING DISTRICT': list_of_values[7]
                }


