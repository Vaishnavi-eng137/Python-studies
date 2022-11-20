#How to create lambda function

#first normal function to add integer 5 in given number
def add_five(num):
    result = num +5
    return result

x = 7
print(add_five(x))

#same program using lambda function
lambda_add_five = lambda x : x+5
y = 10
print(lambda_add_five(y))

#write a lambda function to add two input number
lambda_add_two_nums = lambda x,y : x+y
x=3
y=5
print(lambda_add_two_nums(x,y))

#write a lambda function to concatenate two input strings

lambda_add_two_strings = lambda x,y : x+y
x = input("Enter first string:")
y = input("Enter second string:")
print(lambda_add_two_strings(x,y))

#Write a lambda function to calculate max of two numbers

lambda_calc_max_two = lambda x,y :x if x>y else y
a = 6
b = 8
print(lambda_calc_max_two(a,b))

#How to work with map(),filter(),reduce()

#implement map function
list1 = [1,2,3,4,5,6,7,8]

#Result
#expected result = [1,4,9,16,25,36,49,64]

square_num = lambda x:x*x
square_list = list(map(square_num,list1))
print(square_list)

#Add sequential respective elements in two given lists
list_a = [9,7,6]
list_b = [6,4,3]

sum_two_list = lambda x,y: x+y
sequence_list = list(map(sum_two_list,list_a,list_b))
print(sequence_list)

#How to use reduce?

#To add all the bumbers present in a list
import functools
list_x = [3,4,6,7]

add_two_nums = lambda x,y:x+y
result = functools.reduce(add_two_nums, list_x)
print(result)

multiply_two_nums = lambda x,y:x*y
result = functools.reduce(multiply_two_nums,list_x)
print(result)

#How to use filter

seq = [1,23,4,9,6]

filter_even_num = lambda x:x%2==0 
result=list(filter(filter_even_num, seq))
print(result)

filter_odd_num = lambda x:x%2 !=0 
result=list(filter(filter_odd_num, seq))
print(result)
