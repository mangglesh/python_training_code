#first if else
x = 5
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10
print(x, y, z)


##################### replacement for switch ###############
a=2
if a==2:print("i am 2")
if a==3:print("i am 3")
if a==4:print("i am 4")
if a==5:print("i am 5")
else:print("i dont know who i am :D")


######## simpler aproach for some codes #######
a = "no"
if a == "no":
    b=0
else:
    b=1
# same as 

a = "no"
b = 0 if a == "no" else 1
print(b)




############################ loops codes ########################
u, v, x, y = 0, 0, 100, 30
while x > y:
    u+=1
    x-=1
    if x < y + 2:
        x = 0
    else:
        x = y - 2
print(u, v)
############################### while else loop #################
u, v, x, y = 0, 0, 100, 30
while x > y:
    u+=1
    x-=1
    if x < y + 2:x = 0
    else:x = y - 2
else:
    print('i am in else')
print(u, v)

item_list = [3, "string1", 23, 14.0, "string2", 49, 64, 70]


################################## for loop example ##################
#loop finds the first occurrence of an integer that is divisible by 7
item_list = [3, "string1", 23, 14.0, "string2", 40, 64, 70]
for x in item_list:
    if not isinstance(x, int):
        continue
        print("i will not get printed")
    if not x % 7:
        print("found an integer divisible by seven: %d" % x)
        break
else:print("i found nothing")

##################### range function #######################
#in java for i=0:i++:i<10
list(range(10))
#between a range
#in java for i=3:i++:i<10
list(range(3, 10))
#in java for i=30:i++:i<10
list(range(30, 10))


# between some range with steps
#in java for i=3:i+2:i<10
list(range(3, 10, 2))

#reverse of the range with step
list(range(5, 3, -1))



########################################33 list #####################
#A list in Python is much the same thing as an array in Java or C or any other language.
#  It’s an ordered collection of objects. You create a listd by enclosing a commaseparated list of elements in square brackets, like so
# here we dont need to specify size of list it can grow and shrink on demand

# Python lists can contain different types of elements
# a list element can be any Python object. Here’s a list that contains a variety of
# elements:
# First element is a number, second is a string, third is another list.
x = [2, "two", [1, 2, 3]]

#Modifying lists(beacuse its mutable)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[len(x):] = [5, 6, 7]
x
x[:0] = [-1, 0]
x
x[1:-1] = []
x

#append operator to append single element at the last of the list (in place)
x = [1, 2, 3]
x.append("four")
x



#what if i want to append a list onto other list 
x = [1, 2, 3, 4]
y = [5, 6, 7]
x.append(y)
x #this wont work as it will apend the list as a element

x = [1, 2, 3, 4]
y = [5, 6, 7]
x.extend(y)
x
#insert function
x = [1, 2, 3]
x.insert(6, "hello")
print(x)
x.insert(0, "start")
print(x)


x = ['a', 2, 'c', 7, 9, 11]
del x[1]
x
del x[:2]
x


#reverse in place 
x = [1,2,3,4,5,6,7,8,9]
x.reverse()
#sort on the list 
x = [3, 8, 4, 0, 2, 1]
x.sort()
x

#how to copy to new list
x = [2, 4, 1, 3]
y = x[:]
y.sort()
y
x

# The sort method can sort just about anything, because Python can compare just about
# anything. But there is one caveat in sorting. The default key method used by sort
# requires that all items in the list be of comparable types. That means that using the
# sort method on a list containing both numbers and strings will raise an exception

x = [1, 2, 'hello', 3]
x.sort()


x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
x.sort()
x


#custom sorting 


x = (4, 3, 1, 2)
y = sorted(x)
y
#some operations on list
3 in [1, 3, 4, 5]
True

#operators on list 
z = [1, 2, 3] + [4, 5]
z

[1,2,3,4]*2

min([3, 7, 0, -2, 11])
max([3, 7, 0, -2, 11])



#index fucntion 
x = [1, 3, "five", 7, -2]
x.index(7)
x.index(5)

#count fucntion 
x = [1, 2, 2, 3, 5, 2, 5]
x.count(2)
x.count(5)
x.count(4)



l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
for i in range(len(l)):
    print("my index is ",i," my value is ",l[i])


###############################
x = [1, 2, 3, 4,5]
y = ['a', 'b', 'c'] 
z = zip(x, y)
list(z)
#enumerarte function

#########################################################################################

# tupple
#a tuple is a sequence that is enclosed by ( and )
# tuple in immutable
x = ('a', 'b', 'c')
x[2]
x[1:]
len(x)
max(x)
min(x)
5 in x
5 not in x
#The main difference between tuples and lists is that tuples are immutable.
x[2] = 'd' #will give an error
x + x
x*2

#One-element tuples need a comma
a = (2) #wont work
a = (2,) #will work


#tupple paking and unpacking 


#As a convenience, Python permits tuples to appear on the left-hand side of an assignment operator, in which case variables in the tuple receive the corresponding value
#from the tuple on the right-hand side of the assignment operator. Here’s a simple
(one, two, three, four) = (1, 2, 3, 4)
one
two
#abive can be written sinply by 
one, two, three, four = 1, 2, 3, 4
a = 1, 2, 3, 4, 5 

#some intersting permutations
x = (1, 2, 3, 4)
a, b, *c = x
a, b, c
a, *b, c = x
a, b, c
*a, b, c = x
a, b, c
a, b, c, d, *e = x
a, b, c, d, e



########################################################3 sets ##############################
#mutable
#unordered
#unique

x = set([1, 2, 3, 1, 3, 5])
x
x.add(6) 
x.remove(5) 
1 in x 
4 in x 
y = set([1, 7, 8, 9])
x | y # set union 
x & y  #set intersaction
x ^ y  # symmetric difference



################################################################## dictionary codes demo ##############################

## difference between list and dictionary 
l = []
d = {}

#l[0] = "pp" # it will give error
d["p"] = "pp"
d
d["p"] = "otherpp" #it will update d
d


english_to_french = {}
english_to_french['red'] = 'rouge'
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'
print("red is", english_to_french['red'])


#it will give arror to access the key which is not present 
#english_to_french["orange"]

#alternate
if "orange" in english_to_french:
    a = english_to_french["orange"]
else:
    a = None


#alternatively
#2nd argument is defaulr value in case if key is not present
english_to_french.get("orange","default value")

print(english_to_french.get('blue', 'No translation'))
print(english_to_french.setdefault("orange","i dont know french"))

english_to_french.update({"new french word":"french translation","a":"e"})

#small example to put thibgs toghether 
sample_string = "To be or not to be"
occurrences = {}
for word in sample_string.split():
    occurrences[word] = occurrences.get(word, 0) + 1
for word in occurrences:
    print("The word", word, "occurs", occurrences[word], \
    "times in the string")


#the key inside dictionary should always be inmuttable
#like if i am developing a phone directory then i want both first and last name 
phone_directory  = {
    ("mangglesh","dagar"):98798789689632,
    ("xyz","lstxwz"):47365834658356
}
phone_directory[("mangglesh","dagar")]
computed_results = {}
#dictionaries with keys as the tupples are also used for dynamic programing
#appication 
import time
def time_consuming_funct(arg_1,arg_2,arg_3):
    if (arg_1,arg_2,arg_3) in computed_results:
        return computed_results[(arg_1,arg_2,arg_3)]
    time.sleep(10)
    computed_results[(arg_1,arg_2,arg_3)] = arg_1+arg_2+arg_3
    return arg_1+arg_2+arg_3



a = {"a":1,"b":2,"c":3,"d":3,"d":4,"e":5}
#reversing the dictionary
{v:k for k,v in a.items()}

{v:i for i,v in enumerate(a)}

a = ["a","b","c"]




class A:
     def __init__(self, val):
         self.val = val
     def __repr__(self):
         return f'<A({self.val})>'
     def __add__(self, other):
         print(f'Summing {self} + {other}')
         return A(self.val + other)

A(42) + 10
Summing A(42) + 10
<A(52)>
A(42) + 10 + 100
Summing A(42) + 10
Summing A(52) + 100




c = []
l = [1,2,3,4,5,6,7,8,9]
for i in l:
    if i%2 == 0:
        c.append(i)
print(c)

[i for i in range(10) if i%2 == 0]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[i**2 for i in l]


def func():
    return "i am fucntions"

#assignment question please use the following string and make the next string as upper case after period? and give back the result

a = """We talked before about the difference between evaluating a Python expression interactively and printing the result of the same expression using the print function.
Although the same string is involved, the two operations can produce screen outputs
that look different. A string that is evaluated at the top level of an interactive Python
session will be shown with all of its special characters as octal escape sequences, which
makes clear what is in the string. Meanwhile, the print function passes the string
directly to the terminal program, which may interpret special characters in special
ways. For example, here’s what happens with a string consisting of an a followed by a
newline, a tab, and a b"""

a.split()
word[-1] == "."