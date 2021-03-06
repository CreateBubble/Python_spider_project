import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    # 如果你请求的参数是html结尾的 不需要加/
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//span[@class="font-arial"]/text()')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)

