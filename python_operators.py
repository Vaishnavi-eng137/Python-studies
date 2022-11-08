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
