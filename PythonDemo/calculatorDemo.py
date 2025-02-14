class Calculator:
    num = 100 #class variables

    #default constructor
    def __init__(self,a ,b):
        self.firstNum = a
        self.secondNum = b
        print("I am automatically created when object is called")

    def countSum(self):
        return self.firstNum + self.secondNum + self.num

    def getData(self):
        print("I'm now executing calculator class")

obj = Calculator(2 ,3) #syntax to create objects in python
print(obj.countSum())