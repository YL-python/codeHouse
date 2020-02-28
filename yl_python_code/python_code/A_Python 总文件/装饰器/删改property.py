class Goods(object):
    def __init__(self):
        # 商品原价
        self.original_price = 100
        # 商品折扣
        self.discount = 0.8

    @property
    def price(self):
        val= self.original_price *self.discount
        return val

    @price.setter   # property 的属性名.setter
    def price(self,value):
        print('price.setter')
        self.original_price = value

    @price.deleter   # property的属性名.deleter
    def price(self):
        print('price.deleter')
        del self.original_price

obj = Goods()
print(obj.price)  # 获取商品价格
obj.price = 456   # 修改商品原价
print(obj.price)
del obj.price     #删除商品原价
obj.price