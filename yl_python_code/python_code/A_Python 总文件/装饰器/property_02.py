class Pager:
    def __init__(self,current_page):
        # 表示用户请求的页码
        self.current_page = current_page
        # 表示每页默认显式的数据数
        self.per_item = 10

    @property
    def start(self):
        val = (self.current_page-1) * self.per_item
        return  val

    @property
    def end(self):
        val = self.current_page * self.per_item
        return val

P = Pager(1)
print(P.start)
print(P.end)

# 定义property让开发者跟在意返回值 而不是实现过程
# 吧实现过程封装 让开发者想获取一个值的时候 就像调用了属性一样
# 不用考虑我调用的时候是否要传参数