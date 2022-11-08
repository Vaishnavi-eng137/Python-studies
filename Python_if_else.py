#how to use if_else in python
x = 10
y = 20

if x==y :
    print("Yes,X is Equals to Y !!")
else:
    print("No, x is not equals to Y !!")

# is it necessary to use else block with if?        

a = 50

if a == 50:
    print("Yes ,a is equals to 50 !!")

print("bye !!")

# else if condition 

marks = 30

if marks < 20 :
    print("score more" )
elif marks >=20 and marks<30:
    print("good to go")    
elif marks >=30 and marks<=40:
    print("excellent")    
else :
    print("please check your marks again !!")
