str1 = "JeromeSampleString.com.ph"
str2 = "JeromeSubstringTest"
str3 = "Jerome"

print(str1[0]) # will print J
print(str2[1:4]) # will print ero
print(str1 + str2) #concatenation of string
print(str3 in str1) #will find if string in st3 is visible in str1

var = str1.split(".") #split string into list
print(var)
print(var[0])

str4 = " great "
print(str4.split()) #remove whitespace in string
