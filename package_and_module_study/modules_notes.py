#What is a module?
# A module is a file containing code. A module defines a group of Python functions or
# other objects, and the name of the module is derived from the name of the file.

#In Python, it’s trivial—you refer to them in your main program as mymodule.reverse and othermodule.reverse.
#Python uses namespaces
#A namespace is essentially a dictionary of the identifiers available to a block, function, class, module, and so on
# but be aware that each module has its own namespace, and this helps avoid naming conflicts


# But the new definitions aren’t directly accessible
import my_math
import my_math_2
#pi wont work
print(my_math.pi)

from my_math import pi
print(pi)
#print(area()) #wil give error


#now lets try to fool python
from my_math import pi
from my_math_2 import pi
print(pi)
my_math.area

# type of import statements 
import my_math
#from modulename import name1, name2, name3, . . . 


#The * stands for all the exported names in modulename
# import those that don’t begin with an underscore

from my_math import * # makes more dificult for reader to understand the code
print(_t)
print(_volume())
print(area())
print(pi)
print(__b)

# get __all__ in module


# But if a list of names called __all__ exists in the module (or the package’s
# __init__.py), then the names are the ones imported, whether they begin with an
# underscore or not
# this is how a module developer can restrict the exposed code or variable

from my_math import _t
print(_t)
#private variables 


# Although you can use the __all__ attribute to hide names from from ...
# import * by not listing those names, this is probably not a good idea, because it’s
# inconsistent. If you want to hide names, make them private by prefacing them
# with an underscore.






################# name spaces in python ###########
######### a litle pinch how its done #########################3
#  A namespace in Python is a mapping 
#  from identifiers to objects and is usually represented as a dictionary

#When a
#block of code is executed in Python, it has three namespaces: local, global, and built-in



#local----> global -----> build-in 

#at the start of script the global and local namespaces are the same
# Creating any variable or
# function or importing anything from another module results in a new entry

# But when a function call is made, a local
# namespace is created, and a binding is
# entered in it for each parameter of the call.
# A new binding is then entered into this local
# namespace whenever a variable is created
# within the function


# The global namespace
# of a function is the global namespace of the
# containing block of the function 
print()
def sample_fucn(g = None):
    i = 100
    print("i am in fucntion ")
    print(locals().keys())
print(locals().keys())







#######################################33 python serach path ############
#Exactly where Python looks for modules is defined in a variable called path

import sys
sys.path
#  Regardless of the details, the string indicates a list
# of directories that Python searches (in order) when attempting to execute an import
# statement. The first module found that satisfies the import request is used
# sys.path initialised from PYTHONPATH
#first python script is inserted automaticaly
locals()
globals()
# dont do tis mistake somtime we take python too much forgranted
i = 18
def sample_fucntion(d =90):
    i = 10 
    print("loacal entry--->",locals())
    print("global entry ---->",globals().keys())
    print(i)

sample_fucntion(99)



import p_folder.p_module
from p_folder.p_module import p

