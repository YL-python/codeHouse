"""
设计正则表达式，从上面字符串中获取出以下内容：
1）  [110000,北京市]
2）  [[110000,北京市],[110101,东城区],[110102，西城区]]
"""

import re

html_str = '''
<tbody>

    <tr height="19" style="mso-height-source:userset;height:19px">

          <td height="19" style="height:19px"></td>

          <td>110000</td>

          <td>北京市</td>

          <td></td>

     </tr>

     <tr height="19" style="mso-height-source:userset;height:19px">

          <td height="19" style="height:19px"></td>

          <td>110101</td>

          <td><span style="mso-spacerun:yes">   </span>东城区</td>

          <td></td>

     </tr>

     <tr height="19" style="mso-height-source:userset;height:19px">

          <td height="19" style="height:19px"></td>

          <td>110102</td>

          <td><span style="mso-spacerun:yes">   </span>西城区</td>

          <td></td>

     </tr>

</tbody>
'''

p1 = re.compile('<td height="19" style="height:19px"></td>(.*?)<td></td>', re.S)
p2 = re.compile('<td>(.*?)</td>', re.S)
data1 = re.findall(p1, html_str)
data = list()

for i in data1:
    data2 = re.sub(r"[\s]", '', i)
    data3 = re.findall(p2, data2)
    data4 = list()
    data4.append(data3[0])
    data4.append(data3[1][-3:])
    data.append(data4)

print(data[0])
print(data)
