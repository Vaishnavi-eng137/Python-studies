#write a program to print from 1 to 10 using 2 steps
#To print odd numbers starting from  value 1
# range(1,11) --> [1,2,3,4,5,6,7,8,9,10] gives us a list
for num in range(1,11,2):
    print(num)

#write a program to print from 10 to 1
for num in range(10,0,-1):
    print(num)

#declare or create a list
int_list = [1,3,5,8,9]

#write a program to cal. the sum of given list elements using for loop

int_list = [4,8,-2,10,5]
sum = 0
for num in int_list:
    sum += num
print("Total sum of list:",sum)

