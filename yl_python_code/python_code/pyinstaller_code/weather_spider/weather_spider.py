import requests
import city
from lxml import etree


class WeatherSpider:
    def __init__(self, key):
        self.key = key
        num = city.fun(key)
        self.url = 'http://www.weather.com.cn/weather/{}.shtml'.format(num)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/74.0.3729.131 Safari/537.36'}
        self.day_list = list()
        self.weather_list = list()
        self.temperature_list = list()
        self.wind_list = list()

    # 1 请求数据
    @property
    def get_data(self):
        data = requests.get(self.url, headers=self.headers, timeout=1.0).content.decode('utf-8')
        # print(data)
        Xpath_data = etree.HTML(data)
        return Xpath_data

    # 2 分析数据
    def analyse_data(self, data):
        self.day_list = data.xpath('//div[@id="7d"]/ul/li/h1/text()')

        self.weather_list = data.xpath('//div[@id="7d"]/ul/li/p/@title')

        self.temperature_list = list()
        for i in range(1, 8):
            temperature_1 = data.xpath('//div[@id="7d"]/ul/li[{}]/p[@class="tem"]/span/text()'.format(i))
            temperature_2 = data.xpath('//div[@id="7d"]/ul/li[{}]/p[@class="tem"]/i/text()'.format(i))
            if not temperature_1:
                temperature = temperature_2[0]
            else:
                temperature = temperature_1[0] + '/' + temperature_2[0]
            self.temperature_list.append(temperature)

        self.wind_list = list()
        wind = data.xpath('//div[@id="7d"]/ul/li/p[@class="win"]/i/text()')
        for i in wind:
            x = i
            self.wind_list.append(x)

    # 3 表现数据
    def print_data(self):
        print(self.key + '的近七天天气如下：')
        print('|{x:^{y}s}\t|'.format(x='天气', y=15 - len('天气'.encode('GBK')) + len('天气'))
              + '{x:^{y}s}\t|'.format(x='气象', y=15 - len('气象'.encode('GBK')) + len('气象'))
              + '{x:^{y}s}\t|'.format(x='温度', y=15 - len('温度'.encode('GBK')) + len('温度'))
              + '{x:^{y}s}\t|'.format(x='风力:', y=20 - len('风力'.encode('GBK')) + len('风力')))
        for i in range(7):
            # print(self.day_list[i].rjust(10),end='')
            print('|{x:^{y}s}\t'.format(x=self.day_list[i],
                                        y=15 - len(self.day_list[i].encode('GBK')) + len(self.day_list[i])), end='')
            # print(self.weather_list[i].rjust(10),end='')
            print('|{x:^{y}s}\t'.format(x=self.weather_list[i],
                                        y=14 - len(self.weather_list[i].encode('GBK')) + len(self.weather_list[i])),
                  end='')
            # print(self.temperature_list[i].rjust(10),end='')
            print('|{x:^{y}s}\t'.format(x=self.temperature_list[i],
                                        y=14 - len(self.temperature_list[i].encode('GBK')) + len(
                                            self.temperature_list[i])), end='')
            # print(self.wind_list[i].rjust(10))
            print('|{x:^{y}s}\t|'.format(x=self.wind_list[i],
                                         y=20 - len(self.wind_list[i].encode('GBK')) + len(self.wind_list[i])))

    def pep8_data(self):
        data_str = self.key + '近七天的天气如下:\n'
        title_str = '|{x:^{y}s}\t|'.format(x='日期', y=20 - len('日期'.encode('GBK')) + len('天气')) \
                    + '{x:^{y}s}\t|'.format(x='气象', y=20 - len('气象'.encode('GBK')) + len('气象')) \
                    + '{x:^{y}s}\t|'.format(x='温度', y=20 - len('温度'.encode('GBK')) + len('温度')) \
                    + '{x:^{y}s}\t|'.format(x='风力:', y=20 - len('风力'.encode('GBK')) + len('风力'))
        data_str += title_str + '\n'

        for i in range(7):
            day = '|{x:^{y}s}\t'.format(x=self.day_list[i],
                                        y=15 - len(self.day_list[i].encode('GBK')) + len(self.day_list[i]))
            weather = '|{x:^{y}s}\t'.format(x=self.weather_list[i],
                                            y=15 - len(self.weather_list[i].encode('GBK')) + len(self.weather_list[i]))
            temper = '|{x:^{y}s}\t'.format(x=self.temperature_list[i],
                                           y=15 - len(self.temperature_list[i].encode('GBK')) + len(self.temperature_list[i]))
            wind = '|{x:^{y}s}|'.format(x=self.wind_list[i],
                                        y=15 - len(self.wind_list[i].encode('GBK')) + len(self.wind_list[i]))
            data = day + weather + temper + wind
            data_str = data_str + data + '\n'
        return data_str

    def Run(self):
        Xpath_data = self.get_data
        self.analyse_data(Xpath_data)
        # self.print_data()
        return self.pep8_data()


if __name__ == '__main__':
    ans = 0
    name = input('输出要查城市的名字：')
    WS = WeatherSpider(name)
    WS.Run()
    # try:
    #     WS = WeatherSpider(name)
    # except:
    #     print('我已经很努力了，可是还没有找到这个地方')
    #     ans = 1
    # if ans:
    #     pass
    # else:
    #     WS.Run()

'''
'{x:^{y}s}\t|'.format(x='温度',y=15 - len('温度'.encode('GBK')) + len('温  度'))   
这里+len('温  度')   温度之间加了空格是因为  加空格 就能跳到下一个制表位

py虽好，有些细节还是没有照顾到中文
这里补齐长度时中文字符也按1字节计算了，
然而我们知道，utf-8中中文占用3个字节，GBK中占用了2个字节，只算作1字节显然不能对齐
固定长度输出就可以这样
len = 固定长度 - len('中文内容'.encode('GBK')) + len('中文内容')

format函数的使用见这个链接   https://www.runoob.com/python/att-string-format.html
'''
