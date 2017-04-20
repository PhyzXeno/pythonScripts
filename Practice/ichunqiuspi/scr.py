import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.ichunqiu.com/courses/all-all-0-0-0-2-1',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                # 'text': quote.css('span.text::text').extract_first(),
                'name': quote.xpath('/html/body/div[4]/div[2]/ul/li[2]/div/div/div[2]/div[1]/div[1]').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)