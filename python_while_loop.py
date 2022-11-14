# print a table of 9
num = 9 
counter= 1

while(counter <= 10):#either true or false
    ans = num*counter
    print(num,'*',counter,'=',ans)
    counter +=1

# what will happen if counter not incremented?
# a popular error stackoverflow will happen
#it will get stuck in infinite loop
# while count


#what will happen?
while True:
    print("iNeuron") 
# I have explicitly mentioned boolean true ,so this will also get stuck in infinite loop
