#Declare empty list
L1 = []
print(type(L1))

#since list is a data structure it comes with methods
#each type of data structure is kind of class
#object-->physical entity of the class

#Insert values in list
L1.append(5)
L1.append(6)
L1.append(7)
print(L1)

#create a list of 1000 numbers start from 1 to 1000
# int_list = []
# for num in range(1,1001):
#     int_list.append(num)

#How to cal. length of a list
len_of_list = len(L1)
print("length of list:",len_of_list)

#how to check if lists are equal to each other
list1 = [1,'shalu',78]
list2 = [1,'shalu',78]
print("Comparing lists are equal ?",list1 == list2)

list1 = [1,'shalu',78]
list2 = [1,78,'shalu']
print('lists are equal??',list1 == list2)

list3 = [1,2,3]
list4 = [89,78,676]
result = list3 + list4
print(result)

#how to access list values
list6 = [2,3,5,7,9,'k','p']

#print all elements of given list ---1
for num in list6:
    print(num)

#2nd element
print(list6[1])

#what will happen --> gives index error
# print(list6[100]) #list index out of range 

list7 = [1,'high',90]

#how to update value of list index item 
#update 'high to 'low'

list7[1] = 'low'
print(list7)

#how to prinnt list elements using length

for i in range(0,len(list7)):
    print(list7[i])

list8 = [1,23,'shalu',[9,7],'gita']
print(len(list8)) #--> 5

#Diff between append() & extend()
list9 = [0,56,90]
list10 = ['ki','lo'] # --> considered this list as one single element
list9.append(list10) #--> does not return anything we can't assihn it to any variable here
print('Output of Append:',list9)

list9 = [0,56,90]
list10 = ['ki','lo'] # --> it will pull out the elements one by one
list9.extend(list10)
print('Output of Append:',list9)

#output of append = [0,56,90,['ki','lo']] --> length is 4
#output of extend = [0,56,90,'ki','lo'] -->extends the length of list--> length is 5

#list slicing
list11 = [3,4,5,6,7,7,8,33,89]
#syntax --> list_name[start:end]
print(list11[0:])  #starts from 0th index & goes till last element
print(list11[ : ]) #entire list will get printed
print(list11[0:4]) #or [ :4] # starts from 1st element to 3rd index element since end index is always exclusive.
print(list11[2:6]) # starts from 2nd index element & ends at 5th index element
print(list11[0: :2]) #3rd parameter is step size i.e 2 here


# reverse the list elements  BY DEFAULT STEP PARAMETER IS POSITIVE
print(list11[::-1])
print(list11[-1: :-1])


#HOW TO PRINT LAST VALUE OF LIST?
print(list11[-1]) #print last element without knowing length of list
print(list11[len(list13)-1])
