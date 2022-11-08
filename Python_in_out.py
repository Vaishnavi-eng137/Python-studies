# Declare & assign variables in python 

int_var = 19
float_var = 67.09
string_var = 'ñāḥōō' #ōr anōṭḥer̥ way "hello"
bool_var = True #or False

# Function in Python for output
# function --> they might or might not accept parameters
print("Shalu is awesome")

#print variable values in python
'''until and unless something is not inside sinle or double quotes
that will ot be treated as space after comma'''
print('value of int_var =',int_var,'--> result done')
print('value of float_var =',float_var,"--> result done")
print('value of string_var = ',string_var)
print('value of bool_var = ',bool_var)

#how to check data type of any variable?
#we can use type()
print("Type of int_var ?",type(int_var))
print("Type of float_var ?",type(float_var))
print("Type of string_var ?",type(string_var))
print("Type of bool_var ?",type(bool_var))

# How to do the type casting?
# data type is something that we can change 
# for eg. int type can be changes to string or to float type 
# int(),float(),str(),bool()
int_var = int_var +10  #int_var = 10+19 & then int_var is 29
casted_int_var = float(int_var) #int_var = float(int_var)
casted_float_var = int(float_var)

print('int to float typecasting for int_var = ',casted_int_var)
print("float to int typecasting for float_var = ",casted_float_var)

numeric_str = "1213"
#numeric_str = numeric_str + 50 # is it valid ? can only concatenate str (not "int") to str

numeric_str = int(numeric_str) + 50 # numeric_str = int('1213') + 50 --> 1213 + 50
print("Value of numeric_str = ",numeric_str)

#how to take inputs in python?
#we can use input() function

'''name = input()
age = input()
print("user name = ",name)
print("user age = ",age)'''

# python file_name.py (manual way to run python code or
# to run input()       go to play buttton option & select run python file  )

#another way to take user input with cutom message
name = input("enter value for name = ")
age = input("enter value for age = ")
print("user name = ",name)
print("user age = ",age)
