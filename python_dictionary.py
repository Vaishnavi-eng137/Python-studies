#Dictionary in python
dict1 = {}
print(type(dict1))

#How to insert values in Dictionary
dict2 = {}
dict2['name'] = 'rēśḥāṁ'
dict2['age'] = 67
dict2['skills'] = ['Python','Javascript']
dict2['states visited'] = ('Jharkhand','Punjab','Delhi')
dict2[56] = 'Random Key'

dict3 = {'color':'skyblue','nation':'Indian'}
dict2['other details'] = dict3
print(dict2)

#check the length of dictionary, --> total no. of key value pairs
print(len(dict2))

#How to access value of a particular key
print(dict2['name'])

#How to update value of a particular key
dict2['age'] = 90

print(dict2['skills'][1]) 
#--> accessing from a list inside dictionary
print(dict2['other details']['nation'])
#--> accessing from a dictionary inside dictionary

#How to get the keys and typecasting into a list from a dictionary
total_keys = list(dict2.keys())
print('Total keys in dictionary:',total_keys)

#How to get values from a dictionary
total_values = list(dict2.values())
print('Total values in dictionary:',total_values)

#How to iterate on Dictionary
for k,l in dict2.items():
    print("keys is",k,'and value is',l)

#Compare dictionary 
#--> gives true bcz it compares the values with keys not by sequence
dict3 ={'n':'polo',9:90}
dict4 = {9:90,'n':'polo'}
print(dict3==dict4)

#--> gives false bcz value is not same
dict3 ={'n':'polo',9:90}
dict4 = {9:90,'n':'pl'}
print(dict3==dict4)

#How to delete specific key value pair in dictionary --> deletes the object and its references
del(dict2['age'])
del(dict2[56])

def factorial(n):
    if n==0 or n==1:
        return 1
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result  
  
print(factorial(3))

#How to check if keys exists in dictionary
keys_in_dict = list(dict2.keys())
if 'skills' in keys_in_dict:
    print(True)
else:
    print(False)    
