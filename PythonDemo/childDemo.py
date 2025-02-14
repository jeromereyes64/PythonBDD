#from filename import class
from PythonDemo.calculatorDemo import Calculator

class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def getMoreData(self):
        return self.num2 + self.num + self.countSum()

obj2 = Child()
print(obj2.getMoreData())
print(obj2.getData())