#more efficient way to read/write file
# with open('test.txt','r') as reader:
#     content = reader.readlines()
#     reversed(content)
#     with open('test.txt', 'w') as writer:
#         for line in reversed(content):
#             writer.write(line)
#         print(writer.readlines)


#reading data from the file
obj = open("test.txt", "a")
obj.write("this is a new file")
obj.close()