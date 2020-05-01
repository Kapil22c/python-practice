from collections import OrderedDict  # needed in code below

#This file contains tuples remaining items and dictionary full 

#Python tutorial file 2
lib1={'3 idiots','dangal','amirs movie'}
lib2={'bala','article 15','ayushyman','dangal'}

movie=lib1.union(lib2)
movie1=lib1.intersection(lib2)
movie2=lib1.difference(lib2)
movie3=lib2.difference(lib1)
print(movie)
print(movie1)
print(movie2)
print(movie3) 
m=movie3.clear()
print(m)


#Dictionaries
# they are good at super organized data ( mini databases)
# Fast as hell (constant time)

groceries= {'banana':5,'mangoes':6}
print(groceries['banana'])  # if key is not present then return error
print(groceries.get('apple'))# if key is not present then return NONE and will not generate error

contacts = {
'Joe': ['52521-22','kk@web.com'],
'Jane' : ['7844-555','gg@gmail.com']  # we can make list in dictionaries
}

print(contacts['Joe'])
# we can make dictionaries in dictionaries itself

contacts2 = {
'Joe': {'phone':'52521-22','mail':'kk@web.com'},
'Jane' : {'phone':'7844-555','mail':'gg@gmail.com'}  # we can make list in dictionaries
}

print(contacts2['Joe'])



sentence="I like the name Kapil,because the name of Kapil is like my name"

word_counts={
    'I':1,
    'like':2,
    'the':2,
    'name':3
}
#addin to a dictionary
print(word_counts)
word_counts['Aaron']=2
print(word_counts)

#dict.items()
print(list(word_counts.items()))

#dict.keys()
print(list(word_counts.keys()))



#dict.values()
print(list(word_counts.values()))

#dict.pop(key)
print(word_counts)

word_counts.pop('name')
print(word_counts)

#dict.popitem()

print(word_counts)
print(word_counts.popitem()) # pops last item from the dictionary
print(word_counts)


#dict.clear()
print(word_counts.clear())

# Ordered dictionary --- for that import OrderDict in starting of the code


# mutability in python
#Mutate= Change
#Mutability=Changable
#Immutability= Unchangable

#List is mutable.... [1,2,3].append(4)
#Tuples is immutable...{1,2,3} can't change it.

#immutate
#tuples
#ints , floats,booleans

#mutate
#lists
#dictionaries
#OrderDict

t=(1,2, [1,2,3])
print(t)
t[2][0]=7
print(t)



