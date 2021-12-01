
# coding: utf-8

# Built-in data types
# Numbers
# 
# 
# Python’s four number types are integers, floats, complex numbers, and Booleans
# 
# 􀂃 Integers—1, –3, 42, 355, 888888888888888, –7777777777
# 􀂃 Floats—3.0, 31e12, –6e-4
# 􀂃 Complex numbers—3 + 2j, –4- 2j, 4.2 + 6.3j
# 􀂃 Booleans—True, False
# points to to be covered for every data types.
# 1. Initialisation
# 2. operators used
# 3. normally used functions for that data type
# 
# 

# Integers
# 

# In[34]:


#initialisation
i = 89
#operators used
#integers with // c results in truncation
print(5 // 3) 
#Division of integers with / b results in a float
print(5 / 3)
print(type(5 / 3))
print(5 % 2)
print(2 ** 8) #power operator



# before jumping to the function on integers part lets first discuss about some basic functions which help to understant any data type in python
# lets take things slow....!

# In[8]:


#basic functions
#dir
dir(int)
i = 0
dir(i)


# In[22]:


#type
i = 3
type(i)
type(i) == int
isinstance(i,int)


# In[19]:


#help function in case if developers friend google is not available  :D
help(i) #will give dicription of class
dir(i)
help(i.real) # will give discription of specific fucntion of that class in some IDEs
help(int.real)


# In[33]:


print(dir(int))
i = 90
i.bit_length()


# Floats
# 

# In[2]:


x = 4.3 ** 2.4
print(x)
type(x)
(3+2j) ** (2+3j)


# In[3]:


3.5e30 * 2.77e45


# In[4]:


#complex numbers
x = (3+2j) ** (2+3j)
print(x.real)
print(x.imag)


# In[6]:


round(6.2)
import math
math.ceil(3.49)


# In[7]:


#Booleans:
x = False
not x
y = True * 2
type(y)
#true and false can act varialbles as well 


# Strings
# String processing is one of Python’s strengths. There are many options for delimiting
# strings:
# 
# "A string in double quotes can contain 'single quote' characters."
# 
# 'A string in single quotes can contain "double quote" characters.'
# 
# '''\tThis string starts with a tab and ends with a newline character.\n'''
# 
# """This is a triple double quoted string, the only kind that can
# contain real newlines."""
# 
# 1. Strings are also immutable
# 2. The operators and functions that work with them return new strings derived from the original
# 3. operators used for strings *,+,in
# 4. build in function are min,max,len
# 
#all about print
# by default prints to stdout but can changed 
# will be explaining how to know about any function in depth
print("i am inside the file",file = open("sample_2.txt","w"))
print("word1","word2",sep = "|",file = open("sample_2.txt","w"),end = "efl")


# In[11]:


x = "live and let \t \tlive"
x.split()

e = 2.718
x = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]
print("The constant e is:", e, "and the list x is:", x)


# In[14]:

e = "i am e"
print("the value of %s is: %0.2f" % ("e", e))
print( "%s is the %s of %s" % ("Ambrosia", "food", "the gods"))

# In[21]:
#advanced features

student_name,e = "mangglesh dagar",77
s = "this is  a string {} and this is the number {} in that string ".format(student_name,e)
print(s)
s1 = "this is  a string {1} and this is the number {0} in that string ".format(student_name,e)
print(s1)
s2 = "this is  a string {} and this is the number in that string ".format(student_name,e)
print(s2)
p = "{food} is the food of {user}".format(food="Ambrosia",user="the gods")
print(p)
#s2 = "this is  a string {} and this is the number {} in that string {}".format(student_name,e)#this will retun a error
#what if we want {} braces in our string
s4 =  "{{Ambrosia}} is the {0} of {1}".format("food", "the gods") 
print(s4)
# You can also use both positional and named parameters, and you can even access attributes and elements within those parameters:
s5 = "{0} is the food of {user[1]}".format("Ambrosia", user=["men", "the gods", "others"]) 
print(s5)
#more advance in python3

s3 = f"this is  a string {student_name} and this is the number {e} in that string "
print(s3)





 #string slicing codes 
 #single attribute
 "0123456789"[0]
 "0123456789"[-1]

#slice 
"0123456789"[1:6]
"0123456789"[6:1]

"0123456789"[2:-3]

"0123456789"[:3]

"0123456789"[-3:]
"0123456789"[-8::2]

# Basic string operations
a = "hello " + "world"
s = "a" * 8 #a will get appended 8 times
"am" in "ia am "

#basic functions
# by default it takes whitespace 
"hey this is python training".split()
"hey:this:is:python:training".split(":",maxsplit = 1)
s = "hey:this:is:python:training".split(":",maxsplit = 2)

# String concatenation using + is useful but not efficient for joining large numbers
# of strings into a single string, because each time + is applied, a new string object is created.A better option is to use the join function

" ".join(s)
" \they am removing white spaces from both sides\n ".strip()
" \they am removing white spaces from right side\n ".rstrip()
" \they am removing white spaces from left side\n ".lstrip()
#explain qrgument of it 


"hey this is python training".islower()
"hey this is python training".replace("hey","hi")

# #find, rfind, index, and rindex.
# Both startswith and endswith can look for more than one string at a time. If the
# parameter is a tuple of strings, both methods check for all of the strings in the tuple
# and return a True if any one of them is found
"mhey this is python training".startswith("m")
"2323456789".startswith(("1","2"))
"hey this hey is python training".find("hey") #starting index if present 
# start and end arguments
"hey this is python hey training".rfind("hey")
"hey this is python training".find("revrevv") #return -1 if not present
"i am similar to find but with a catch".index("amm") #wil give exception
"hey this is python hey training".count("hey")


x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")
x.translate(table)

"6767.77".isdigit()
"676".isdigit()

#somtime we want to directly manipulate the string we can do it through list
a = list("abcdefghijk")
"".join(a)
#relatively expensive

"123456789"[6:0:-1]

#you can do some experiment to play
# string.whitespace
# string.digits
# string.hexdigits
# string.digits
# string.octdigits
# string.lowercase
# string.uppercase
# string.letters
# string.lowercase
# string.uppercase


#spcl
a = 100_000000_000
print("{:,}".format(a))

 







# %%
