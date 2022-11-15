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


def factorial(n):
    if n==0 or n==1:
        return 1
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result  
  
print(factorial(3))
