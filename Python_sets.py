#Sets in Python -->only contains unique values
set1 = set()
print(type(set1))

list1 = [1,3,3,4,4,6,78,0,9] # list contains duplicates so to remove duplicates we typecast list into sets
set2 = set(list1)
print(set2)

#-->taken care during the runtime & does not gives error
set3 = {1,2,3,3,5,9}
print(set3)
print(type(set3))

#--> this will return type as dictionary
set4 ={}
print(type(set4))

#How to iterate on elements of sets
for num in set2:
    print(num) 

list1 = [1,3,3,4,4,6,78,0,9] 
set5 = list(set(list1))
print(set5)
print(set5[-1])

#How to insert elements in set
#Though we have tried to insert multiple duplicates values 
#we will only get distinct values in set
set6 = set()
set6.add(1)
set6.add(3)
set6.add(2)
set6.add(2)
set6.add(5)
print(set6)

#use of update method
temp = [1,2,3,3,4,5,6,7,8]
set6.update(temp)
print(set6)

#length of the set
print(len(set6))

#Set operations --> union or intersection
set_a = {8,9,6,7}
set_b = {9,0,7,3}

#union operation --> getting all values excluding duplicates
print(set_a | set_b)

#intersection operation --> getting common values
print(set_a & set_b)

#difference -->keep all the elements of set_a except which are also present in setb 
print(set_a - set_b)
#difference -->keep all the elements of set_b except which are also present in seta 
print(set_b - set_a)

#comparison in sets 
set_1 = {'x',3,'k','o'}
set_2 = {'x','x',3,'k','o'}
set_3 = {'x','y'}
print(set_1 == set_2) # -->gives True
print(set_1 == set_3) # --> gives false
