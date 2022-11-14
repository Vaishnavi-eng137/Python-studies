#create a string in python , strings are immutable 
# string is also a sequential data structure just like list
str1 = 'ineuron'
str2 = "toyota"
str3 = '''hello 
there'''
print(str3)

#use length function
print("length of the string:",len(str3))

#string concatenation
print(str1+str2)

#string comparison
print(str2 == str3)

#how to print each char from string
for string in str3:
    print(string)
print(str1[1])

#update 4th char in the string by M ,we can't change string values
str3[3] ='M'
print(str3) # --> TypeError: 'str' object does not support item assignment

print(str2.lower())  #-->convert into lower case
print(str2.upper())  #-->convert into upper case
print(str2.title()) # --> converts into proper case
print(str2.capitalize()) # -->converts  first letter into caps.
# print(str2.split , swapcase, find , index , strip ) and many more 

#other functionalities will be same as list like slicing etc
