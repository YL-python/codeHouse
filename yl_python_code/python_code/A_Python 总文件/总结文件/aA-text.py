# import re
# import csv
# x='''(1.486,3.059,0.1);(2.121,4.041,0.1);(2.570,3.959,0.1);
# (3.439,4.396,0.1);(4.505,3.012,0.1);(3.402,1.604,0.1);
# (2.570,2.065,0.1);(2.150,1.970,0.1);(1.794,3.059,0.2);
# (2.121,3.615,0.2);(2.570,3.473,0.2);(3.421,4.160,0.2);
# (4.271,3.036,0.2);(3.411,1.876,0.2);(2.561,2.562,0.2);
# (2.179,2.420,0.2);(2.757,3.024,0.3);(3.439,3.970,0.3);
# (4.084,3.036,0.3);(3.402,2.077,0.3);(2.879,3.036,0.4);
# (3.421,3.793,0.4);(3.953,3.036,0.4);(3.402,2.219,0.4);
# (3.000,3.047,0.5);(3.430,3.639,0.5);(3.822,3.012,0.5);
# (3.411,2.385,0.5);(3.103,3.012,0.6);(3.430,3.462,0.6);
# (3.710,3.036,0.6);(3.402,2.562,0.6);(3.224,3.047,0.7);
# (3.411,3.260,0.7);(3.542,3.024,0.7);(3.393,2.763,0.7)'''
# y = x.split(';')
# p = re.compile(r"\((.*?)\)")
# data_list=[]
# for i in y:
#     data1={}
#     data = p.findall(i)
#     x,y,z=data[0].split(',')
#     data1['x']=x
#     data1['y'] = y
#     data1['z'] = z
#     data_list.append(data1)
# # print(dict)
#
# csv_fp = open("csv.csv","w",newline='')
# sheet_title = data_list[0].keys()
#
# sheet_data = []
# for data in data_list:
#     sheet_data.append(data.values())
# # #创建csv写入器
# writer = csv.writer(csv_fp)
#
# #写入表头 和内容
# writer.writerow(sheet_title)
# writer.writerows(sheet_data)
#
# #关闭打开的文件
# csv_fp.close()


# print('\n'.join([''.join([('Hzz'[(x-y) % len('Hzz')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))



# import re
# str = """
# Y2hlbmppbmdjb25n0+
# Y2hlbmppbmdjb25n1+
# Y2hlbmppbmdjb25n2+
# Y2hlbmppbmdjb25n3+
# Y2hlbmppbmdjb25n4+
# Y2hlbmppbmdjb25n5+
# Y2hlbmppbmdjb25n6+
# Y2hlbmppbmdjb25n7+
# Y2hlbmppbmdjb25n8+
# Y2hlbmppbmdjb25n9+
# Y2hlbmppbmdjb25n10+
# Y2hlbmppbmdjb25n11+
# Y2hlbmppbmdjb25n12+
# Y2hlbmppbmdjb25n13+
# Y2hlbmppbmdjb25n14+
# Y2hlbmppbmdjb25n15+
# Y2hlbmppbmdjb25n16+
# Y2hlbmppbmdjb25n17+
# Y2hlbmppbmdjb25n18+
# Y2hlbmppbmdjb25n19+
# Y2hlbmppbmdjb25n20+
# Y2hlbmppbmdjb25n21+
# Y2hlbmppbmdjb25n22+
# Y2hlbmppbmdjb25n23+
# Y2hlbmppbmdjb25n24+
# Y2hlbmppbmdjb25n25+
# Y2hlbmppbmdjb25n26+
# Y2hlbmppbmdjb25n27+
# Y2hlbmppbmdjb25n28+
# Y2hlbmppbmdjb25n29+
# Y2hlbmppbmdjb25n30+
# Y2hlbmppbmdjb25n31+
# Y2hlbmppbmdjb25n32+
# Y2hlbmppbmdjb25n33+
# Y2hlbmppbmdjb25n34+
# Y2hlbmppbmdjb25n35+
# Y2hlbmppbmdjb25n36+
# Y2hlbmppbmdjb25n37+
# Y2hlbmppbmdjb25n38+
# Y2hlbmppbmdjb25n39+
# Y2hlbmppbmdjb25n40+
# Y2hlbmppbmdjb25n41+
# Y2hlbmppbmdjb25n42+
# Y2hlbmppbmdjb25n43+
# Y2hlbmppbmdjb25n44+
# Y2hlbmppbmdjb25n45+
# Y2hlbmppbmdjb25n46+
# Y2hlbmppbmdjb25n47+
# Y2hlbmppbmdjb25n48+
# Y2hlbmppbmdjb25n49+
# Y2hlbmppbmdjb25n50+
# Y2hlbmppbmdjb25n51+
# Y2hlbmppbmdjb25n52+
# Y2hlbmppbmdjb25n53+
# Y2hlbmppbmdjb25n54+
# Y2hlbmppbmdjb25n55+
# Y2hlbmppbmdjb25n56+
# Y2hlbmppbmdjb25n57+
# Y2hlbmppbmdjb25n58+
# Y2hlbmppbmdjb25n59+
# Y2hlbmppbmdjb25n60+
# Y2hlbmppbmdjb25n61+
# Y2hlbmppbmdjb25n62+
# Y2hlbmppbmdjb25n63+
# Y2hlbmppbmdjb25n64+
# Y2hlbmppbmdjb25n65+
# Y2hlbmppbmdjb25n66+
#
# """
#
# data = re.sub(r"[\s]", '',str)
# print(data)
#
# import time
# for i in range(101):
#     time.sleep(0.1)
#     print("\r正在下载"+str(i)+"%",end='')
