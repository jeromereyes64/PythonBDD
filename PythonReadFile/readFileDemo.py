file = open('test.txt') #open the file.
#print(file.read()) #show the contents in logs

#Read data through while loop
# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

#Read data through For loop
for line in file.readlines():
    print(line)

file.close()