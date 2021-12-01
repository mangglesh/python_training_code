# Numpy is the fundamental package for numeric computing with Python
# # It provides powerful ways to create, store, and / or manipulate data, 
# which makes it able to seamlessly and speedily integrate with a wide variety of databases
# This is also the foundation that Pandas is built on,
# learning NumPy is the first step on any Python data scientist’s journey.(this will make you excited)

# what we will learn 
# 1.What core concepts in data science are made possible by NumPy
# 2.How to create NumPy arrays using various methods
# 3.How to manipulate NumPy arrays to perform useful calculations
# 4.How to apply these new skills to real-world problems

#--------- why numpy -----------
# Here are the top four benefits that NumPy can bring to your code:

# More speed: NumPy uses algorithms written in C that complete in nanoseconds rather than seconds.
# Fewer loops: NumPy helps you to reduce loops and keep from getting tangled up in iteration indices.
# Clearer code: Without loops, your code will look more like the equations you’re trying to calculate.
# Better quality: There are thousands of contributors working to keep NumPy fast, friendly, and bug free.

#just a samll example to know how numpy is great
import numpy as np

digits = np.array([[1, 2, 3],[4, 5, 6],[6, 7, 9]])
digits[digits > 2]



# its made from c internally 
strings_np = np.array(["ecewiscbwjic","qwc"])
strings_np[1] = "ewohcewiobceiocnewi"




import numpy as np
CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12]) 
# the above line is creating the array of size (8,) of data type int64
# we have some more the  syntaxes as well 
# which will define some spcl types of numpy array
#
np.zeros((2, 3))
np.ones((2, 3))
# np.twos((1,2)) not there :D
np.random.rand(2, 3)
np.arange(10, 50, 2)
np.linspace(0, 2, 15)
#will give 15 numbers from 0 (inclusive) to 2 (inclusive)


b = np.array([[1, 2, 3], [4, 5, 6]])
# We can print out the length of each dimension by calling the shape attribute, which returns a tuple
b.shape

# We can also check the type of items in the array
b.dtype
b.dtype.name

# same code in python
farenheit = [0, -10, -5, -15, 0]
[(i - 31) * (5/9) for i in farenheit]
# same numpy code you can see here 
# you can write code as if you are writing maths equation.

farenheit = np.array([0, -10, -5, -15, 0])
celcius = (farenheit - 31) * (5/9)
celcius


#code redability is awesome right 




# now lets see operations on arrays 


""" 
in operations on array you take advantage of two important concepts at once:
1. Vectorization
2. Broadcasting

Vectorization is the process of performing the same operation in the same way for each element in an array.
This removes for loops from your code but achieves the same result.

Broadcasting is the process of extending two arrays of different shapes and figuring out
how to perform a vectorized calculation between them. Remember, grades is an array of 
numbers of shape(8,) and change is a scalar, or single number, essentially with shape(1,).
In this case, NumPy adds the scalar to each item in the array and returns a new array with
the results.

it functions around one rule: 
arrays can be broadcast against each other if their dimensions match or if one of the arrays
has a size of 1.
 """

B = np.ones((1, 7))
A = np.ones((3, 1))
A + B

# some bigger example 
A = np.arange(32).reshape(4, 1, 8)
B = np.arange(48).reshape(1, 6, 8)
C = A + B
C.shape

# A lot of times, you’ll have to simply follow the broadcasting rules 
# and do lots of print-outs to make sure things are working as planned.

# Understanding broadcasting is an important part of mastering vectorized calculations, and
# vectorized calculations are the way to write clean, idiomatic NumPy code.

# Arithmetic operators on array apply elementwise.

# some more operations
# Let's create a couple of arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Now let's look at a minus b
c = a-b
print(c)

# And let's look at a times b
d = a*b
print(d)

# Besides elementwise manipulation, it is important to know that numpy supports matrix manipulation. Let's
# look at matrix product. if we want to do elementwise product, we use the "*" sign
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A*B)
# if we want to do matrix product, we use the "@" sign or use the dot function
print(A@B)

""" The scenario is this: You’re a teacher who has just graded your students on a recent test.
Unfortunately, you may have made the test too challenging, and most of the students did 
worse than expected. To help everybody out, you’re going to curve everyone’s grades.
 """

grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
CURVE_CENTER = 80

def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


curve(grades)

#Understanding Axes
# In NumPy arrays, axes are zero-indexed and identify
# which dimension is which. For example, a two-dimensional array has a vertical axis(axis 0)
# and a horizontal axis(axis 1). Lots of functions and commands in NumPy change their 
# behavior based on which axis you tell them to process.

# This example will show how .max() behaves by default, with no axis argument, and how it 
# changes functionality depending on which axis you specify when you do supply an argument

table = np.array([
[5, 3, 7, 1],
[2, 6, 7, 9],
[1, 1, 1, 1],
[4, 3, 2, 0]])
table.max()
table.max(axis=0)
table.max(axis=1)


# --------------------------------------------------------------------------
# Indexing
# indexing uses many of the same idioms that normal Python code uses. You can use positive 
# or negative indices to index from the front or back of the array.
# Here’s the difference: NumPy arrays use commas between axes,
import numpy as np

square = np.array([
     [16, 3, 2, 13],
     [5, 10, 11, 8],
     [9, 6, 7, 12],
     [4, 15, 14, 1]
])
square[1,1]
square[1,2]
#row,cloumn
square[1,1:]
square[2:,1:3]

# Masking and Filtering
# if you want to filter your data based on more complicated nonuniform or nonsequential criteria?
# This is where the concept of a mask comes into play.

# A mask is an array that has the exact same shape as your data, but instead of your values, 
# it holds Boolean values: either True or False.

numbers = np.linspace(5, 50, 24, dtype=int).reshape(4, -1)
mask = numbers % 4 == 0
numbers[mask]
by_four = numbers[numbers % 4 == 0]

numbers[(numbers % 4 == 0) & (numbers % 10 == 0)]
# It’s because NumPy designates & and | as the vectorized,
#  element-wise operators to combine Booleans
numbers[(numbers % 4 == 0) and (numbers % 10 == 0)] # it wont work 


#Transposing, Sorting, and Concatenating


a = np.array([
[1, 2],
[3, 4],
[5, 6],
])

a.T
a.transpose()
data = np.array([
[7, 1, 4],
[8, 6, 5],
[1, 2, 3]
])

np.sort(data)
np.sort(data, axis=None)
np.sort(data, axis=0)

# concatenation

a = np.array([
[4, 8],
[6, 1]
])

b = np.array([
[3, 5],
[7, 2],
])

np.hstack((a, b))

np.vstack((b, a))

np.concatenate((a, b))

np.concatenate((a, b), axis=None)

#Aggregating

#something like .sum(), .max(), .mean(), and .std()

#datatypes
# in NumPy, though, there’s a little more detail that needs to be covered. NumPy uses C code
# under the hood to optimize performance, and it can’t do that unless all the items in an array 
# are of the same type. That doesn’t just mean the same Python type. They have to be the 
# same underlying C type, with the same shape and size in bits!




names = np.array(["bob", "amy", "han"], dtype=str)

names
names.itemsize
names = np.array(["bob", "amy", "han"])
names
more_names = np.array(["bobo", "jehosephat"])
np.concatenate((names, more_names))


#Structured Arrays
# NumPy has a special kind of array, called a record array or structured array, 
# with which you can specify a type and, optionally, a name on a per-column basis. 
# This makes sorting and filtering even more powerful, and it can feel similar to working 
# with data in Excel, CSVs, or relational databases.

data = np.array([
("joe", 32, 6),
("mary", 15, 20),
("felipe", 80, 100),
("beyonce", 38, 9001),
], dtype=[("name", str, 10), ("age", int), ("power", int)])
data[0]
data["name"]
data[data["power"] > 9000]["name"]



# so now some real life example to show how much can you do with numpy 
# Let's take a look at another dataset, this time on graduate school admissions. It has fields such as GRE
# score, TOEFL score, university rating, GPA, having research experience or not, and a chance of admission.
# With this dataset, we can do data manipulation and basic analysis to infer what conditions are associated
# with higher chance of admission. Let's take a look.

# We can specify data field names when using genfromtxt() to loads CSV data. Also, we can have numpy try and
# infer the type of a column by setting the dtype parameter to None
graduate_admission = np.genfromtxt('Admission_Predict.csv', dtype=None, delimiter=',', skip_header=1,
                                   names=('Serial No', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
                                          'LOR', 'CGPA', 'Research', 'Chance of Admit'))
graduate_admission
# Notice that the resulting array is actually a one-dimensional array with 400 tuples
graduate_admission.shape
# We can retrieve a column from the array using the column's name for example, let's get the CGPA column and
# only the first five values.
graduate_admission['CGPA'][:5]

# Since the GPA in the dataset range from 1 to 10, and in the US it's more common to use a scale of up to 4,
# a common task might be to convert the GPA by dividing by 10 and then multiplying by 4
graduate_admission['CGPA'] = graduate_admission['CGPA'] / 10 * 4
graduate_admission['CGPA'][0:20]  # let's get 20 values


# Recall boolean masking. We can use this to find out how many students have had research experience by
# creating a boolean mask and passing it to the array indexing operator
len(graduate_admission[graduate_admission['Research'] == 1])


# Since we have the data field chance of admission, which ranges from 0 to 1, we can try to see if students
# with high chance of admission (>0.8) on average have higher GRE score than those with lower chance of
# admission (<0.4)

# So first we use boolean masking to pull out only those students we are interested in based on their chance
# of admission, then we pull out only their GPA scores, then we print the mean values.
print(graduate_admission[graduate_admission['Chance_of_Admit']
                         > 0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']
                         < 0.4]['GRE_Score'].mean())

# When we do the boolean masking we are left with an array with tuples in it still, and numpy holds underneath
# this a list of the columns we specified and their name and indexes
graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]

# Let's also do this with GPA
print(
    graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['CGPA'].mean())
print(
    graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['CGPA'].mean())


# https://github.com/Promeos/numpy-100
# https://www.fullstackpython.com/scipy-numpy.html
