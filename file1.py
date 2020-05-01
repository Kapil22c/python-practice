#Python Path : C:\Users\Kapil\AppData\Local\Programs\Python\Python37


#Python tutorial practice... don't depend on file name 


#import turtle
#my= turtle.Turtle()

#my.speed(500)

def square():
    my.forward(100)
    my.right(90)
    my.forward(100)
    my.right(90)
    my.forward(100)
    my.right(90)
    my.forward(100)
    
    

#for count in range(80):
 #   square()

 # Indexing slicing and sliding
window=5
dig=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(dig)-window+1):
    print(dig[i:i+window])

someString= 'kapil,nehal,bharat,kiran'
z=someString.split(",")
print(z)

# split and join function

joined=' and '.join(z)
print(joined)
csv=' , '.join(z)
print(csv)

#tuple

t={1,2,3}
credit_card1=(50485426582112145,'Kapil bavisiya','6/21',555)
credit_card2=(542226582112145,'Neha; bavisiya','6/21',666)

credit_card=[credit_card1,credit_card2]
print(credit_card)


person1=("nehal-bavisiya", 26, "dosa")
person2=("kanyo-vvd", 22, "ddosa")
people=[person1,person2]
#[name, age, favfood]=person

for name, age , favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()

# list uses [] square bracet
# tuple uses () parenthases
# set uses {} curly braces


#set
s={'blue','red','yellow','black'}
s.add('red')  # this will not add red in set as it is already in there... List will add this value
print(s)


l=[1,2,3,3,3,4,5,5,'abc',"abc"]
no_dup= set(l)
print(no_dup)
no_dup_list= list(no_dup)

print(no_dup_list)


 
