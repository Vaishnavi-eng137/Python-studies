#write a program to generate list of 10 numbers
result = []
for i in range(1,11):
    result.append(i)
print(result)

#How to do it with list comprehension
result = [x for x in range(1,11)]
print(result)

#Get a list of all even numberss between 1 to 50
result = [x for x in range(1,50) if x%2==0]
print(result)

#Get a list of all even numbers from the given list
list_a = [1,2,3,4,5]
result = [x for x in list_a if x%2==0]
print(result)

#Convert all string into upper case in given list
list_b = ['hi','hello','bye','nice']
result = [x.upper() for x in list_b]
print(result)

#put all negative number after positive numbers from given list
list_s = [1,-1,2,9,-5]
result = [x for x in list_s if x>0]
result1 = [x for x in list_s if x<0]
print(result + result1)


