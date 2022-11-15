#Functions in python --> reusability of code 
#what about len()  --> inbuilt function
#EXAMPLES OF INBUILT FUNCTIONS
list1 = [2,3,4]
print("Maximun no. from list:",max(list1))
print("Minimum no. from list:",min(list1))
print("Sum of number from list:",sum(list1))

#How do functions works?
#They may or may not accepts input parameter
#They may or may not return any output

#example of a function which doesn't accept any parameter
def welcome_msg():
    print("hello guys")

welcome_msg()
#example of a function which returns output
def bot_msg():
    return("I am the boss")

result = bot_msg()
print(result)

#example of a function which accepts parameter and return output
def sum(a,b):
    return a+b
print(sum(2,5))

#average function
def average(a,b):
    count = 2
    avg_result = (a+b)//2
    return avg_result

num1 = 6
num2 = 7 
output = average(num1,num2)
print("Result of avg_of_2_numbers:",output)

# factorial function
def factorial(n):
    if n==0 or n==1:
        return 1
    result = 1
    for number in range(1,n+1):
        result = result*number
    
    return result

print("Factorial of number:",factorial(5))

#How to return multiple values from function

a,b,c = 2,3,5
print("Value of a is:",a)
print("Value of a is:",b)
print("Value of a is:",c)

def square_cube(n):
    sqr = n*n
    cube = n*n*n
    return sqr,cube

num = 3
sqr_ans,cube_ans = square_cube(num)
print("square of ",num," is :",sqr_ans)
print("cube of ",num," is :",cube_ans)

#How to create optional arguments in python function
def multiply(a,b=3):
    result = a*b
    return result

#def multiply(a=3,b) what if we reverse this part --> will give error
num1 = 5
num2 = 78
print(multiply(num1,num2)) # it only checks the sequence of arguments which we pass
print(multiply(num1)) #-->2nd arg which we r not provided here then bydefault it will assume num as 3 

#non key valued arguments
def example_non_keyed_args( *args): #-->more readable
    for param in args:
        print(param)

example_non_keyed_args('Hello','Welcome','To',"House")

# connect_to_db('172.80.80.80','lion',9090)
# connect_to_db('lion','172.80.80.80',9090)

#key value type of arguments in Python
def ex_of_kwargs(**kwargs):

    print("Value of host:",kwargs['host'])
    print("Value of port:",kwargs['port'])
    print("Value of password:",kwargs['pswd'])
    for k,v in kwargs.items():
        print("key is",k,'and value is',v)
 

ex_of_kwargs(host='172.80.80.80',port='lion',pswd=9090)
