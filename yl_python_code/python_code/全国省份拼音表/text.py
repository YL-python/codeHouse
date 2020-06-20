cityNameStr = """北京    BeiJing
上海    ShangHai
天津    TianJin
重庆    ChongQing
香港    XiangGang
澳门    Aomen
安徽    AnHui
福建    FuJian
广东    GuangDong
广西    GuangXi
贵州    GuiZhou
甘肃    GanSu
海南    HaiNan
河北    HeBei
河南    HeNan
黑龙江    HeiLongJiang
湖北    HuBei
湖南    HuNan
吉林    JiLin
江苏    JiangSu
江西    JiangXi
辽宁    LiaoNing
内蒙古    NeiMengGu
宁夏    NingXia
青海    QingHai
陕西    ShanXi
山西    ShanXi
山东    ShanDong
四川    SiChuan
台湾    TaiWan
西藏    XiZang
新疆    XinJiang
云南    YunNan
浙江    ZheJiang"""

cityNameList = cityNameStr.split('\n')
# print(cityNameList)
print(len(cityNameList))

nameP = {}
pName = {}

for city in cityNameList:
    cList = city.split("    ")
    name = cList[0]
    pinyin = cList[1].lower()
    nameP[str(name)] = pinyin
    pName[pinyin] = name
print(pName)
print(nameP)
