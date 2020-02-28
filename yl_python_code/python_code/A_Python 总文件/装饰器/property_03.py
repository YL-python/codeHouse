class Money:
    def __init__(self,num):
        self.__money = num

    def Get_data(self):
        print('---get---')
        return self.__money

    def Set_data(self,value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('这里需要一个整数值')

    MONEY = property(Get_data,Set_data)

x = Money(5)
print(x.MONEY)
x.MONEY = 10
print(x.MONEY)