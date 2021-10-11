import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # identifies the Spider

    def start_requests(self): # must return an iterable of Requests
        # which the Spider will begin to crawl from
        urls = [
                'https://www.ziprecruiter.com/Career/Hardware-Engineer/Resume-Keywords-and-Skills'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): # a default callback  method that will be called to handle the response
        # downloaded for each of the requests made, usually parses the response,
        # extracting the scraped dataq as dicts and also finding new URLs to follow
        # and creating new requests from them

        keywords1 = response.xpath('/html/body/div[2]/main/div/section/article/section[4]/div[2]/table/tbody//td[1]//text()').extract()
        keywords2 = response.xpath('/html/body/div[2]/main/div/section/article/section[4]/div[3]/table/tbody//td[1]//text()').extract()
        keywords = list(set(keywords1) | set(keywords2))
        print(keywords)
        yield { 'title': keywords }

