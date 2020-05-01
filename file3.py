#List comprehension
names=['kapil','nehal','naimish','meet']
l=[]
for person in names:
    l.append(person)
print(l)

print([person for person in names])

l =[]
for person in names:
    l.append(person+' dumped me')
print(l)

print([person + ' dumped me' for person in names])

movies_and_ratings={'Intersteller':9,'Dark knight':8,'Fifty shades':1,'mahabharat':10}


l=[]
for movie in movies_and_ratings:
    if movies_and_ratings[movie]>8:
        l.append(movie)
print(l)

print( [movie for movie in movies_and_ratings if movies_and_ratings[movie]>8])




