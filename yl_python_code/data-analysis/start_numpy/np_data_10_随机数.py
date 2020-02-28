import numpy as np

t1 = np.random.rand(2, 3)  # 随机分布的浮点数 [0,1)
t2 = np.random.randn(2, 3)  # 标准正态分布的随机浮点数  平均数是0 标准差是1
t3 = np.random.randint(1, 5, (2, 3))  # 随机分布的整数 范围是[1,5)  形状是（2，3）
t4 = np.random.uniform(1, 5, (3, 4))  # 随机分布的数组1为起始值 5为结束值 形状是(3, 4)
t5 = np.random.normal(5, 2, (3, 4))  # 从指定的正态分布中随机抽取样本，分布中心是5（概率分布的均值） 标准差是2 形状是（3， 4）
np.random.seed(5)  # 随机种子 设置随机种子可以设定生产相同的随机数
