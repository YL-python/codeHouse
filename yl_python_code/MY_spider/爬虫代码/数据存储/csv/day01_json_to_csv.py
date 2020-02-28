#json 转 csv
import json
import csv

#json文件转csv文件 需要读json 和创建csv
json_fp = open("json_to_csv.json","r")
csv_fp = open("csv.csv","w")

#提取出 表头 和内容
data_list = json.load(json_fp)  #吧json文件转成列表

sheet_title = data_list[0].keys()
#中文表头  sheet_title = {"姓名","年龄"}
print(sheet_title)
print(type(sheet_title))

sheet_data = []
for data in data_list:
    sheet_data.append(data.values())

print(sheet_data)

#创建csv写入器
writer = csv.writer(csv_fp)

#写入表头 和内容
writer.writerow(sheet_title)
writer.writerows(sheet_data)

#关闭打开的文件
json_fp.close()
csv_fp.close()