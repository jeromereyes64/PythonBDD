class Sample:

    def __init__(self, a, b):
        print("This is constructor")
        c = a - b
        print(f"the difference is: {c}")

    #print method
    def hello(self):
        print("Hello Test Class")

    #add
    def add(self,a,b):
        c = a + b
        print(f"the sume is {c}")

    #multiply
    def multiply(self,a,b):
        c = a * b
        return c