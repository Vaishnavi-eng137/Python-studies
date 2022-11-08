# Numerical operators 

# + for addition
# - for subtraction
# * for multiplication
# / for float division
# // for integer division
# ** for power calculation
# % for modulus

x = 6
y = 7
print("addition of x+y = ",x+y)
print("subtraction of x-y = ",x-y)
print("multiplication of x*y = ",x*y)
print("float division of x/y = ",x/y)
print("integer division of x//y = ",x//y)
print("modulus of x%y = ",x%y)
print("power of y on x = ",x**y)

# some operations on string
str_data ='vaishnavi'
empty_str = ''

# concat operatios for string
full_name = str_data + ' '+ "kumari"
print("full name  is  = ",full_name)

# we can not use (-),(/),(//),(**) operator  {unsupported operator}
# can't multiply sequence by non-int of type 'str'
# --> multiply_str = 'neha'*'op'
#power_str = str_data ** str_data

multiply_num_str = "vaisu"*5 # this works & gives vaisu 5 times
print(multiply_num_str)

# Assignment operators
# = , x = 5
# +=,x += 5 --> x = x+5
# -=,x -= 5 --> x = x-5
# *=,x *= 5 --> x = x*5
# /=,x /= 5 --> x = x/5
# //=,x //= 5 --> x = x//5
# %=,x %= 5 --> x = x%5

# Comparison operators (we compare operands values)
# ==, Equals to condition, x == y
# !=, not Equals to condition, x != y
# <, Less than condition, x < y
# <=, Less than or equal to condition, x <= y
# >,Greater than condition, x > y
# >=,Greater than or equal to condition, x >= y

a = 22
b = 20

print("result of a==b ", a == b)
print("result of a!=b ", a != b)
print("result of a<=b ", a <= b)
print("result of a>=b ", a >= b)
print("result of a>b ", a > b)
print("result of a<b ", a < b)

# logical operators in Python (logical check will happen for expression result)
# i.e comparing the values of two expression
# and --> returns true if both statements are true and vice versa
# or --> returns true if one of statements are true 
# not --> reverse the result, returns false if the result is true

m = 10
n = 67
print('m>10 and n<10 result', m>10 and n<10) # false and false --> false
print('m>10 or n>10 result', m>10 or n>10) # false or true --> true
print("not(m>10 and n<10) result", not(m<10 and n<10)) # not(true and false) -->true



