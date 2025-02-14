#sample function
def test():
    print("this is my test function")

def sum():
    a = 20
    b = 30
    c = a + b
    print(f"the sum is: {c}")

def multiply(a,b):
    c = a * b
    return c

def addition(a,b):
    c = a + b
    print(c)

sumNum = multiply(10,20)
addition(sumNum,30)

test()
sum()