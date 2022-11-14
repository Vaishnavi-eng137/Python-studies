#Tuples are immutable objects 
#we use tuples when we want to freeze or fix the data
# t1 = () --> it's useless bcz it's immutable
# failed assignment & append
t1.append(5)
t1[0] = 5

t2 = (67,98,43)
print(len(t2))

#indexing,slicing,iteration also works for tuple
#access 3rd element from tuple

print(t2[2])
