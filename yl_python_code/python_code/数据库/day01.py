import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root',
                     password='root', database='test',
                     port=3306, charset='utf8')
