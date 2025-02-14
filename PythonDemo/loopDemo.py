#if else statement
greetings = "good morning"

if greetings == "morning":
    print("not the same")
elif greetings == "good":
    print("still not the same")
else:
    print("now it's the same")


# for loop
value_test = [1, 2, 3, 4, 5]
for i in value_test:
    print(f"this are the values: {i}")


#do the sum sum in for loop
# iterate from 1 to 5. The last digit will always be minus 1
sumNumber = 0
for j in range(1, 6):
    print(f"the numbers are: {j}")
    sumNumber = j + sumNumber
print(f"total loop is: {sumNumber}")



#another method of looping
for j in range(1, 6, 2):
    print(j)
    print("****skip 2 numbers every iteration")


for m in range(20):
    print(m)