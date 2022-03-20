import scrapy
from scrapy_dangdang_095.items import ScrapyDangdang095Item

class DangSpider(scrapy.Spider):
    name = 'dang'
    # 如果是多页下载的话 那么必须要调整的是allowed_domains的范围 一般情况下
    # 只写域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    base_url = 'http://category.dangdang.com/pg'
    page = 1




    def parse(self, response):
#         pipelines 下载数据
#         items 定义数据结构
#         src = response.xpath('//ul[@id="component_59"]/li//img/@src')
#         alt = response.xpath('//ul[@id="component_59"]/li//img/@alt')
#         price = response.xpath('//ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()')
#         所有的selector对象都可再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片和其他图片的属性不一样
            # 第一张的src可以使用 其他的都是data-original
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDangdang095Item(src=src,name=name, price=price)

            # 获取一个book就把book交给piplines
            yield book

#             每一页爬虫的业务逻辑都是一样的 所以我们只需要将执行的
#             的那个页面的请求再次调用prase方法即可
#
#           http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
#           http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
        if self.page < 10:
            self.page = self.page + 1

            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'
            # 怎么去调用prase方法
            # scrapy.Request就是scrapy的get请求
            # url就是请求地址
            # callback是你要执行的那个函数  注意不要加（）
            yield scrapy.Request(url=url,callback=self.parse)