import scrapy
from ..items import BluetomatoItem

class TomatopriceSpider(scrapy.Spider):
    name = 'prices'
    page_number = 2
    start_urls = ['https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/?page=1']

    def parse(self, response):
        items = BluetomatoItem()
        
        #getting values of products with sale
        product_price = response.css('span.productdesc > span.price.sale:first-of-type::text').extract()


        for price in product_price:
            yield{
                
                'product_price': price.strip()
            }

        
        next_page = 'https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/?page=' + str(TomatoSpider.page_number)
        if TomatoSpider.page_number < 35:
            TomatoSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)