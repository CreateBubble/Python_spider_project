import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://wf.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D']
    start_urls = ['https://wf.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D']

    def parse(self, response):
        print('啊啊啊啊啊啊啊啊啊啊啊')
        # 字符串
        print('====' * 30)
        # content = response.text
        # 二进制数据
        # print('===='*30)
        # content = response.body
        # print(content)
        # print('===='*30)
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')
        print('===='*30)
        print(span)