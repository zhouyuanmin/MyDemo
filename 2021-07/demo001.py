class Car:
    def __init__(self, name, loss):
        # loss [价格，油耗，公里数]
        self.name = name
        self.loss = loss

    def get_name(self):
        return self.name

    def get_price(self):
        # 获取汽车价格
        return self.loss[0]

    def get_loss(self):
        # 获取汽车损耗值
        return self.loss[1] * self.loss[2]


print(dir(Car))
