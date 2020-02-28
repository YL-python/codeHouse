import requests
import json
import os


class spider:
    def __init__(self):
        self.url = 'http://www.nmc.cn/f/rest/province'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/74.0.3729.131 Safari/537.36'}
        self.fill_dir = 'lib/JsonData'

    @property
    def yes_no_get(self):
        print("正在测试是否要下载数据！")
        if os.path.exists(self.fill_dir):  # 判断文件夹是否存在
            print("文件夹存在，正在判断数据是否完整！")
            file_len = len([lists for lists in os.listdir(self.fill_dir)])
            if file_len == 35:  # 文件个数是否完整
                print("数据完整，执行下一步！")
                return False
            else:
                print("数据不完整,正在为您下载数据！")
                return True
        else:
            print("文件夹不存在，正在问您创建并下载数据！")
            os.mkdir(self.fill_dir)
            return True

    def get_data(self, url):
        return requests.get(url, headers=self.headers).content.decode("utf-8")

    def seave_data(self, data, path):
        data_list = json.loads(data)
        json.dump(data_list, open(path, "w"))

    def run(self):
        # 判断数据是否完整
        if self.yes_no_get:
            # 请求数据
            response = self.get_data(self.url)
            # 保存数据
            self.seave_data(response,
                            "{}/cityProvince.json".format(self.fill_dir))
            result = json.load(
                open("{}/cityProvince.json".format(self.fill_dir), "r"))
            count = 1
            for temp in result:
                city_name = "/" + temp['url'].split('/')[3].split('.')[0]
                file_name = self.fill_dir + city_name + ".json"
                print("\r"+"正在下载数据：{}/34  ".format(count), end='')
                response = requests.get(self.url + city_name,
                                        headers=self.headers).content.decode(
                    "utf-8")
                self.seave_data(response, file_name)
                count += 1
            print("数据下载完毕")


if __name__ == '__main__':
    A = spider()
    A.run()
