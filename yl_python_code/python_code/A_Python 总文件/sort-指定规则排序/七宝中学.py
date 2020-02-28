import random
print('七宝中学：')
for tno in range(10):
    all_student = 700  # 生成的数据个数
    moni_gailv = [0 for i in range(20)] # 用来计算概率
    # 排序的组合以及并编号
    moni_dic = {
        '政史地':'N01', '生政史':'N02', '生政地':'N03', '生史地':'N04', '物政史':'N05',
        '物政地':'N06', '物史地':'N07', '化政史':'N08', '化政地':'N09', '化史地':'N10',
        '化生政':'N11', '化生地':'N12', '化生史':'N13', '物化政':'N14', '物化地':'N15',
        '物化史':'N16', '物生政':'N17', '物生地':'N18', '物生史':'N19', '物化生':'N20'
        }
    # 概率列表
    N_list = ['物', '物', '物', '物','化', '化', '化', '化','生', '生','生', '生','政', '政', '政','史', '史', '史','地', '地']
    # 文字转数字
    def cn2num(datas):
        item =list()
        dic = {'物':1,'化':2,'生':3,'政':4,'史':5,'地':6}
        for data in datas:
            item.append(dic[data])
        return item
    # 数字转文字
    def num2cn(datas):
        item = list()
        dic = {1:'物',2:'化',3:'生',4:'政',5:'史',6:'地'}
        for data in datas:
            item.append(dic[data])
        return item
    # 蒙特卡洛模拟
    for i in range(all_student):
        itm = list()
        while True:
            x = random.sample(N_list, 1)
            if x not in itm:
                itm.append(x)
            if len(itm) == 3:
                break
        itm = [str(i[0]) for i in itm]
        num_itm = cn2num(itm)
        num_itm.sort()
        cn_itm=(num2cn(num_itm))
        moni_N = ''.join(cn_itm)
        var = moni_dic[moni_N]
        index = int(var[1:]) -1
        moni_gailv[index] += 1
    print('第{}次模拟数据：'.format(tno+1),moni_gailv)
