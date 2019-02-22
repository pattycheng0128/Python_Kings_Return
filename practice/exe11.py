class Operator():

    # def __init__(self, uname):
    #     self.name = uname

    def add(self, a, b):
        sum = a + b
        print("相加:", sum)

    def sub(self, a, b):
        sum = a - b
        print("相減:", sum)

    def mul(self, a, b):
        sum = a * b
        print("相乘:", sum)

    def div(self, a, b):
        sum = a / b
        print("相除:", sum)


test = Operator()
test.add(5, 2)
test.sub(5, 2)
test.mul(5, 2)
test.div(10, 2)