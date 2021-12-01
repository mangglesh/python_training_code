def fact(n):
    """Return the factorial of the given number.""" #its an optional documentation string 
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r #will return the value just like any other language
print("i am out this fucntion")
fact(6)
# You can obtain its value by printing fact.__doc__. 
# The intention of docstrings is to describe the external behavior of a function and the parameters it takes,
#usually triple quoted to allow for multiline descriptions.
help(fact)
fact.__doc__

#when there is no return None is returned 

def fucnt_1():
    """ i am just a fucntion 
    explaining what happens if no return is there"""
    print("i am in funct_!")

print(str(fucnt_1()))

# Function parameter options

# Positional parameters
# Passing arguments by parameter name
# Variable numbers of arguments
# Mixing argument-passing techniques

# Positional parameters


# In the first
# line of the function, you specify definition variable names for each parameter
# when
# the function is called, the parameters used in the calling code are matched to the
# function’s parameter variables based on their order

def power(x, y):
    r = 1
    while y > 0:
        r = r * x
        y = y - 1
    return r
power(3, 3)
power(3) # will give error

# Default values


def power(x , y = 2):
    return x**y

# . Parameters with default values
# must be defined as the last parameters in the parameter list.
#will give an error
def power(x=2, y):
    return x**y

# Passing arguments by parameter name


# i can do this as well
power(y=2, x=3)

#both will give error
power(2,x = 3)
power(y = 2,3)

#Variable numbers of arguments

# You can do this two different ways

# One way handles the relatively familiar case where you
# wish to collect an unknown number of arguments at the end of the argument list into
# a list.

# The other method can collect an arbitrary number of keyword-passed arguments, which have no correspondingly named parameter in the function parameter
# list, into a dictionary. These two mechanisms are discussed next

#lets see each way one by one

# Prefixing the final parameter name of the function with a *
# will take all positional arguments in the tuple
#this type of variable length argumant is also called as agrs
def maximum(*numbers):
    print(numbers)
    print(type(numbers))
    if len(numbers) == 0:
        return None
    else:
        return max(numbers)

maximum(1,2,3,4,5,6,7,8,9,10)
# will give error
maximum(1,a =3)

#An arbitrary number of keyword arguments can also be handled. 
# If the final parameter in the parameter list is prefixed with **,
# it will collect all excess keyword-passed arguments into a dictionary.
#this type of variable length argumant is also called as kagrs

def fucnt3(x,y,**others):
    print("i have positional parameter as -->",x)
    print("i have named parameter as -->",y)
    print("i have name other parameter as -->", others)

fucnt3(2,3,r=5,g=6)

#will give error
fucnt3(2,3,4,5,6,7)
fucnt3(r=5, g=6,2,3)

def fucnt3(x,y,*positional,**others):
    print("i have positional parameter as -->",x)
    print("i have named parameter as -->",y)
    print("i have named parameter as -->",positional)
    print("i have name other parameter as -->", others)
fucnt3(1,2,3,4,5,6,7,a=3)
fucn

# Mutable objects as arguments
# be very carefull with this 

# if you pass in a mutable object(for example, a list, dictionary, or class instance), any change made to the
# object will change what the argument is referencing outside the function


def f(n, list1, list2):
    list1.append(3)
    list2 = [4, 5, 6]
    n = n + 1 

x = 5       #integer is inmutable
y = [1, 2]  #list is mutable
z = [4, 5]
f(x, y, z)
x, y, z

#Local, nonlocal, and global variables

a = 10
def test_fucntion():
    print("iam able to access ouside vriable",a)
test_fucntion()

a = 10
def test_fucntion():
    print("iam not able to change ouside fucntion",a)
    a = "one"

test_fucntion() #will give error

def test_fucntion():
    print("iam not able to change ouside fucntion")
    global a
    a = "one"
test_fucntion()
print(a)



#but for sake of redability dont use global only use it in very few senerios

#Assigning functions to variables

def test_2():
    print("i am test2 fucntion")
a = test_2
a()



#lambda function 
# are one liner fucntions 
def fucnt(input_var):
    print("i am input variable", input_var)

a = lambda input_var:print("i am input variable",input_var)
a(2)


# some good syntax
def test_fucntion(a:str,b:int):
    print(a,b)

test_fucntion("wcjwqb",2)
# but it wont stop you to do mistake
test_fucntion("cqcs","scscw")



# some good example to take care 
#Yes, using None is both safe and conventional in such cases.
# will only be a problem when you change the value of default
def f(value, key, hash={}):
    hash[value] = key
    return hash


print(f('a', 1))
print(f('b', 2))


#map function
# map() function returns a map object(which is an iterator) of the 
# results after applying the given function to each item of a given iterable (list, tuple etc.)

def f(x): return x**2
f = lambda x:x**2

l = [1, 2, 3, 4, 5, 6, 7, 8]
list(map(f, l))


for i in map(f, l):
    print(i)

#filter function 
f = lambda x: x % 2 == 0
list(filter(f,l))

from functools import reduce
#reduce 
l = [1, 2, 3, 4, 5, 6, 7, 8]
f = lambda x,y: x+y
reduce(f,l) 

