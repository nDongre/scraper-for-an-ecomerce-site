import scrapy
from ..items import BluetomatoItem

class TomatoSpider(scrapy.Spider):
    name = 'tomato'
    page_number = 2
    start_urls = ['https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/?page=1']

    def parse(self, response):
        items = BluetomatoItem()

        product_name =  response.css('.track-load-producttile::attr(data-productname)').extract()
        product_price = response.css('span.price::text').extract()
        product_brand = response.css('.track-load-producttile::attr(data-brand)').extract()
        product_image_url = response.css('span.productimage img::attr(data-src)').extract()
        product_url = response.css('.track-load-producttile::attr(href)').extract()


        for name,price,brand,image_url,url in zip(product_name,product_price,product_brand,product_image_url,product_url):
            yield{
                'product_name' : name.strip(),
                'product_price': price.strip(),
                'product_brand': brand.strip(),
                'product_image_url': image_url.strip(),
                'product_url': url.strip()
            }

        #handling pagination.
        next_page = 'https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/?page=' + str(TomatoSpider.page_number)
        if TomatoSpider.page_number < 35:
            TomatoSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)