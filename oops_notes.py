#OOPs in python 
# the fields of an instance don’t need to be declared ahead of time but can be created on the fly
# You can initialize fields of an instance automatically by including an __init__ initialization method in the class body
# same way we have this in java we have self keyword in python 
class Circle:
    def __init__(self):
        print("i am in init fucntion")
        print(self)
        self.radius = 1 #intance variable
my_circle = Circle()
print(2 * 3.14 * my_circle.radius)
my_circle.radius = 5
print(2 * 3.14 * my_circle.radius) 

# self is always the name of the first argument of __init__.
# self is set to the newly created circle instance when __init__ is run
#  We can also overwrite the radius field

#If the variable doesn’t already exist, it’s created automatically. 
my_circle.variable = 1000

my_circle_2 = Circle()
my_circle_2.class_var = 78
Circle.class_var = 789700 #class variable 
print(my_circle.class_var) #even class variable automaticaly copied to instance
my_circle_2.class_var



# Methods

# A method is a function associated with a particular class

class Circle:
    def __init__(self):        
        self.radius = 1
    def area(self):
        return self.radius ** 2 * 3.14159

c = Circle()
c.area()
Circle.area()
c.radius = 3

print(Circle.area(c)) #never used these days
print(c.area()) # both the code does tha same thing


class Circle:
    def area():
        print("i am in class area fucntion")
    def __init__(self, radius):
        self.radius = radius # here radius local fucntion variable and self.radius in instance var 
    def area(self):
        return self.radius ** 2 * 3.14159

c = Circle(5)

c.area() #comment area(self) while explaining 
Circle.area(self)
# while invocating the fucntion 
#  Python transforms it into a normal function call by using the following rules:

# 1   Look for the method name in the instance namespace. If a method has been
#     changed or added for this instance, it’s invoked in preference over methods in
#     the class or superclass. This is the same sort of lookup discussed later in section

# 2   If the method isn’t found in the instance namespace, look up the class type
#     class of instance, and look for the method there. In the previous examples,
#     class is Circle—the type of the instance c.
# 3   If the method still isn’t found, look for the method in the superclasses.
# 4   When the method has been found, make a direct call to it as a normal Python,
#     using instance as the first argument of the function, and shifting all the other
#     arguments in the method invocation one space over to the right. So,
#     instance.method(arg1, arg2, . . .) becomes class.method(instance,
#     arg1, arg2, . . .).




#Class variables
#   A class variable is a variable associated with a class, not an instance of a class, and is
#   accessed by all instances of the class,

class Circle:
    pi = 3.14159 # class variables 
    def __init__(self, radius):
        
        self.radius = radius
    def area(self):
        print(f"class specific value as {Circle.pi}")
        #print(f"class specific value as {self.__class__.pi}")
        print(f"instance specific value as {self.pi}") # if you thing object in spcl case can can have value use this
        return self.radius * self.radius * Circle.pi #i am accessing class variable using class name 
c = Circle(44)
Circle.pi
c.pi
c.area()
Circle.pi = 4
Circle.pi
c.area()
c.pi
c.pi = 66
Circle.pi
c.pi 
Circle.pi = 100
c.pi    # this happened because now at line 87
        # search will end in object itself

c.area() #will have pi value as 100 taking from the class 

#need to explain this 


###############################################################3
#dont use hard coding of class as in line 80 and 82
#we have spcl variable for that as well __class__
#This attribute returns the class of which the instance is a member
Circle
c.__class__ # both gives same thing
#This lets us obtain the value of Circle.pi from c without hard coding
#ever explicitly referring to the Circle class name
c.__class__.pi

# so replace  replace Circle.pi with self.__class__.pi.
#use class variable to have default values to 
# avoid the time and memory overhead of initializing that instance variable every time a class instance
# is created

#If you want to change the
#value of a class variable, access it through the class name, not through the instance
#variable self

####################################################

#Static methods
#Just as in Java, you can invoke static methods even though no instance of that class has
#been created

#you can also call them using a class instance
#  use the @staticmethod decorator

class Circle:
    """Circle class"""
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius

    @staticmethod
    def total_area():
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total
Circle.total_area() # can be called woithout an instance as well

c1 = Circle(1)
c2 = Circle(2)
Circle.total_area()
c2.radius = 3
Circle.total_area()

# it helps to access help for your class
Circle.__doc__
Circle.area.__doc__
help(Circle)


# Class methods
# Class methods are similar to static methods in that they can be invoked before an
# object of the class has been instantiated or by using an instance of the class. But class
# methods are implicitly passed the class they belong to as their first parameter

class Circle:
    """Circle class"""
    all_circles = []
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius
    @classmethod
    def total_area(cls):  # here we use cls instead of self.__class__
        #print(self) will give error
        print("circle ",Circle)
        print("cls var",cls)
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total

Circle.total_area()
c1 = Circle(1)
c2 = Circle(2)
Circle.total_area()
c2.radius = 3
Circle.total_area()



# By using a class method instead of a static method, we don’t have to hardcode the
# class name into total_area. That means any subclasses of Circle can still call
# total_area and refer to their own members, not those in Circle. 
# so subclass will able to use its own variables and and functions

######################################################################
#inheritance

# The second and more subtle element is the necessity to explicitly call the
# __init__ method of inherited classes
# If this weren’t done, then in the example, instances of Circle
# and Square wouldn’t have their x and y instance variables set
#super.__init__() same as  Shape.__init__(self, x, y), 
# which could lead to a problem
# problem later if the design and the inheritance hierarchy change
# if i dont want to use the search seq then i can hard code not done mostly
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y
class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        print("i am super variable",super)
        super().__init__(x, y) # so super will initalise the parent class as well 
        self.side = side        # comment it and explain
class Circle(Shape):
    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r

c = Circle(1)
s = Square(3)
c.move(3, 4)

c.x


c.y

#point to remember only intance variable can have only one variable at a time
class P:
    z = "Hello"
    def set_p(self):
        self.x = "Class P"
    def print_p(self):
        print(self.x)
class C(P):
    def set_c(self):
        self.x = "Class C"
    def print_c(self):
        print(self.x)
# to make search path more clear
c = C()
c.set_p()
c.print_p()
c.print_c()
c.set_c()
c.print_c()
c.print_p()

# not same happens with class variables 
c.z, C.z, P.z
C.z = "hi"
# now things will change it will form new variable in class c
c.z, C.z, P.z
c.z = "obj hi"
c.z, C.z, P.z

#Private variables and private methods

#A private variable or private method is one that can’t be seen outside of the class
#of the class in which it’s defined
#  A class may define a private variable and
# inherit from a class that defines a private variable of the same name, but this doesn’t
# cause a problem, because the fact that the variables are private ensures that separate
# copies of them are kept.
class Mine:
    def __init__(self):
        self.x = 2
        self._g = 9
        self.__y = 3
    def print_y(self):
        print(self.__y)
m = Mine()

print(m.x)
#print(m.__y) ## will give error
m.print_y()
m.__y
dir(m) # if you see carefully we have jugaad here 
m._Mine__y = 8
# Finally, you should note that the mechanism used to provide privacy is to mangle the
# name of private variables and private methods when the code is compiled to bytecode.
# What specifically happens is that _classname is appended to the variable name:

# used in debugging is made easy
###################################3 getter and setter ######################
# This lack of getters and setters makes writing Python classes cleaner and easier; but in some situations, using getter and setter methods can be handy. Suppose you
# want a value before you put it into an instance variable or where it would be handy to
# figure out an attribute’s value on the fly
a = 6
class Temperature:
    def __init__(self):
        self._temp_fahr = 0
    @property   #this is getter
    def temp(self):
        print("i am inside getter")
        return (self._temp_fahr - 32) * 5 / 9
    @temp.setter #this is setter
    def temp(self, new_temp):
        print("i am inside setter")
        self._temp_fahr = new_temp * 9 / 5 + 32


t = Temperature()
t.a = 60
t.a
t = Temperature()
t._temp_fahr
t.temp
t.temp = 34
t._temp_fahr
t.temp

class LowerTextClass:
    def __init__(self):
        self.lower_text = ""
    @property   #this is getter
    def temp(self):
        print("i am inside getter")
        return self.lower_text
    @temp.setter #this is setter
    def temp(self, new_temp):
        print("i am inside setter")
        self.lower_text = new_temp.lower()
    def myfucnt():


l = LowerTextClass()
l.temp = "JCBEWICBEWICBEWCOIE"
l.lower_text

































# for i in {"a":1,"b":2,"c":5}.items():
#     setattr(t,i[0],i[1])
# for i in {"a":1,"b":2,"c":5}:
#     print(getattr(t,i[0]))


t._temp_fahr
t.temp
t.temp = 34
t._temp_fahr
t.temp
