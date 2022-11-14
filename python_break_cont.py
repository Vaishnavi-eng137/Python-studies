#how to use break statement
int_list = [1,2,8,0,56,78]
#find the even value in the given list if only one even value exists.
for integer in int_list:
    if integer%2==0:
        print("First even number in the list:",integer)
        break

#what if break is removed ,it will print all the numbers
for integer in int_list:
    if integer%2==0:
        print("First even number in the list:",integer)

#how to use continue keyword?
#print the numbers from for loop & start them from value 1 
# print values on terminal if number>10

for number in range(1,21):
    if number<10:
        continue
    print(number)            
