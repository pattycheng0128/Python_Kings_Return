class Operator:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def add(self):
        sum = self.__num1 + self.__num2
        print("%d+%d=%d" % (self.__num1, self.__num2, sum))

    def sub(self):
        sum = self.__num1 - self.__num2
        print("%d-%d=%d" % (self.__num1, self.__num2, sum))

    def mul(self):
        sum = self.__num1 * self.__num2
        print("%d*%d=%d" % (self.__num1, self.__num2, sum))

    def div(self):
        sum = self.__num1 / self.__num2
        print("%d/%d=%d" % (self.__num1, self.__num2, sum))


test = Operator(6, 2)
test.add()
test.sub()
test.mul()
test.div()