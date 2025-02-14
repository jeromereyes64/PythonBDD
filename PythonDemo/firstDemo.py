print("Hello")

# here are the comments i have defined


a = 3
print(a)

Str = "Hello World"
print (Str)

b, c, d = 5, 6.4, "Great"
print(b)
print(c)
print(d)
print(f"Value is {b}")


# create integer
intNumber = 12345

#create float
fltNumber = 1.245

#create complex
cpxNumber = 100+3j

print(f"The type of variable {intNumber}", "is ", type(intNumber))
print(f"The type of variable {fltNumber}", "is ", type(fltNumber))
print(f"The type of variable {cpxNumber}", "is ", type(cpxNumber))


#declare a list
values = [1, 2 ,3 ,"string me", 4]

print(values[0])
print(values[-1])
print(values[0:3])
values.insert(3, "add new") #insert new variable
print(values)

values.append("end") #add at the end
print(values)

values[1] = "jtest" #update
print(values)

del values[0] #delete record 1
print(values)

#declare a tuple (Tuple is like enums, it doesn't change

tplValue=(1,2,3, "test")
print(tplValue)

#declare a dictionary
dic = {"a": 2, 4: "jerome test", "c": "Hello World"}
print(dic[4])
print(dic["c"])


#add and create dictionaries
dict = {}
dict["fname"] = "Jerome"
dict["lname"] = "Reyes"
print(dict)