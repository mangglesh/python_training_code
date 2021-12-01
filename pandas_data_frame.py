# Pandas DataFrames are data structures that contain:
# -> Data organized in two dimensions, rows and columns
# -> Labels that correspond to the rows and columns

# There are several ways to create a Pandas DataFrame. In most cases, you’ll use the DataFrame
# constructor and provide the data, labels, and other information. You can pass the data as a 
# two-dimensional list, tuple, or NumPy array. You can also pass it as a dictionary or Pandas 
# Series instance, or as one of several other data types not covered in this tutorial.

# For this example, assume you’re using a dictionary to pass the data:
import numpy as np
import pandas as pd
data = {
'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
'age': [41, 28, 33, 34, 38, 31, 37],
'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }

row_labels = [101, 102, 103, 104, 105, 106, 107]

df = pd.DataFrame(data=data, index=row_labels)

df
# Pandas DataFrames can sometimes be very large, making it impractical to look at all 
# the rows at once. You can use .head() to show the first few items and .tail() to show the last 
# few items:
df.head(n=2)
df.tail(n=2)

#You can access a column in a Pandas DataFrame the same way you would get a value from a
#dictionary:

cities = df['city']
cities


# If the name of the column is a string that is a valid Python identifier, then you can use dot 
# notation to access it. That is, you can access the column the same way you would get the 
# attribute of a class instance:
df.city

type(df.city)
# Each column of a Pandas DataFrame is an instance of pandas.Series, a structure that holds 
# one-dimensional data and their labels.

cities[102]

#You can also access a whole row with the accessor .loc[]
df.loc[103]


# As already mentioned, there are several way to create a Pandas DataFrame. In this section, 
# you’ll learn to do this using the DataFrame constructor along with:

# Python dictionaries
# Python lists
# Two-dimensional NumPy arrays
# Files

import pandas as pd
d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
pd.DataFrame(d)

# It’s possible to control the order of the columns with the columns parameter and the row 
# labels with index:

pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])

l = [{'x': 1, 'y': 2, 'z': 100},
{'x': 2, 'y': 4, 'z': 100},
{'x': 3, 'y': 8, 'z': 100}]
pd.DataFrame(l)

#You can also use a nested list as the input as well
l = [[1, 2, 100],
[2, 4, 100],
[3, 8, 100]]
pd.DataFrame(l, columns=['x', 'y','z'])


arr = np.array([[1, 2, 100],
[2, 4, 100],
[3, 8, 100]])
arr.shape

df_ = pd.DataFrame(arr, columns=['x', 'y', 'z'])
df_

# Although this example looks almost the same as the nested list implementation above, 
# it has one advantage: You can specify the optional parameter copy.

# When copy is set to False (its default setting), the data from the NumPy array isn’t copied. 
# This means that the original data from the array is assigned to the Pandas DataFrame. If you 
# modify the array, then your DataFrame will change too:

arr[0,2] = 10000
arr
df_


#Creating a Pandas DataFrame From Files

# You can save and load the data and labels from a Pandas DataFrame to and from a number 
# of file types, including CSV, Excel, SQL, JSON, and more. This is a very powerful feature.


df.to_csv("data.csv")


#Now that you have a CSV file with data, you can load it with read_csv():

pd.read_csv('data.csv', index_col=0)

#index_col = 0 specifies that the row labels are located in the 
# first column of the CSV file



#Retrieving Labels and Data
# 1. Retrieve and modify row and column labels as sequences
# 2. Represent data as NumPy arrays
# 3. Check and adjust the data types
# 4. Analyze the size of DataFrame objects

#Pandas DataFrame Labels as Sequences
df.index
df.columns

df.columns[1]

df.index = np.arange(10, 17)
df.index
df

#Keep in mind that if you try to modify a particular item of .index or .columns, 
#then you’ll get a TypeError.
#df.index[9] = 88 #wont work


#we can even covert dataframes to numpy array using .to_numpy() and .values()

df.to_numpy()
df.values



#Data types

df.dtypes

df_ = df.astype(dtype = {"age": np.int32,"py-score":np.float32})
df_.dtypes

# The most important and only mandatory parameter of .astype() is dtype. It expects a data 
# type or dictionary. If you pass a dictionary, then the keys are the column names and the 
# values are your desired corresponding data types.

#Pandas DataFrame Size

# The attributes .ndim, .size, and .shape return the number of dimensions, number of data 
# values across each dimension, and total number of data values, respectively
df_.ndim
df_.shape
df_.size


#Accessing and Modifying Data

df['name']
#df.loc[10] # wont work 


#Getting Data With Accessors
df.loc[10]
df.iloc[0]
df.loc[:, 'city']
df.iloc[:,:3]

df.iloc[:, 1]

df.loc[10:11, ['name', 'city']]
df.iloc[:, [0, 1]]
df.loc["b":"e", ["city"]]

# when you need only a single value, Pandas recommends using 
# the specialized accessors .at[] and .iat[]
df.at[10, 'name']
df.iat[2, 0]

#Setting Data With Accessors

df.loc[:, 'py-score']

df.loc[:13, 'py-score'] = [40, 50, 60,70]
df.loc[:13, 'py-score']
df.loc[14:, 'py-score'] = 0
df
df["z":]
# The statement df.loc[:13, 'py-score'] = [40, 50, 60, 70] modifies the first four items(rows 10 through 13)
# in the column py-score using the values from your supplied list. Using 
# df.loc[14:, 'py-score'] = 0 sets the remaining values in this column to 0.

df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
df['py-score']


#Inserting and Deleting Data

# Pandas provides several convenient techniques for inserting and deleting rows or columns. 
# You can choose among them based on your situation and needs.

#Inserting and Deleting Rows

john = pd.Series(data=['John', 'Boston', 34, 79],index=df.columns, name=17)
john
john.name
#
# The new object has labels that correspond to the column labels from df. That’s why you 
# need index = df.columns.

#You can add john as a new row to the end of df with .append():


df = df.append(john)
df

# You’ve appended a new row with a single call to .append(), and you can delete it with a 
# single call to .drop():
df = df.drop(labels=[17])
df

# Here, .drop() removes the rows specified with the parameter labels. By default, it returns 
# the Pandas DataFrame with the specified rows removed. If you pass inplace = True, then the 
# original DataFrame will be modified and you’ll get None as the return value.


#Inserting and Deleting Columns
# The most straightforward way to insert a column in a Pandas DataFrame is to follow the 
# same procedure that you use when you add an item to a dictionary. Here’s how you can 
# append a column containing your candidates’ scores on a JavaScript test:

df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
df
df['total-score'] = 0.0
df

#location of the new column is important, then you can use .insert() instead
df.insert(loc=4, column='django-score',value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
df

# You can delete one column from a Pandas DataFrame just as you would with a 
# regular Python dictionary, by using the del statement

del df['total-score']
df

df = df.drop(labels='age', axis=1)
df

#Applying Arithmetic Operations

# ou can apply basic arithmetic operations such as addition, subtraction, multiplication, and 
# division to Pandas Series and DataFrame objects the same way you would with NumPy arrays:

df['py-score'] + df['js-score']
df['py-score'] / 100

df['total'] = 0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
df
del df["total"]

df['total'] = np.average(df.iloc[:, 2:5], axis=1,weights=[0.4, 0.3, 0.3])


#Sorting a Pandas DataFrame

#You can sort a Pandas DataFrame with .sort_values()

df.sort_values(by='js-score', ascending=False)


# This example sorts your DataFrame by the values in the column js-score. The parameter by 
# sets the label of the row or column to sort by. ascending specifies whether you want to 
# sort in ascending(True) or descending(False) order, the latter being the default setting. 
# You can pass axis to choose if you want to sort rows(axis=0) or columns(axis=1).

# If you want to sort by multiple columns, then just pass lists as arguments for by and 
# ascending:

df.sort_values(by=['total', 'py-score'], ascending=[False, False])
#Filtering Data
# Data filtering is another powerful feature of Pandas. It works similarly to indexing 
# with Boolean arrays in NumPy.


# If you apply some logical operation on a Series object, then you’ll get another Series with 
# the Boolean values True and False:

filter_ = df['django-score'] >= 80
filter_

df[filter_]


#You can create very powerful and sophisticated expressions by combining logical operations 
# with the following operators:

# 1. NOT(~)
# 2. AND ( & )
# 3. OR ( | )
# 4. XOR ( ^ )

# For example, you can get a DataFrame with the candidates whose py-score and js-score are 
# greater than or equal to 80:
df[(df['py-score'] >= 80) & (df['js-score'] >= 80)]


df['django-score'].where(cond=df['django-score'] >= 80, other=0.0)


# In this example, the condition is df['django-score'] >= 80. The values of the DataFrame or 
# Series that calls .where() will remain the same where the condition is True and will be 
# replaced with the value of other (in this case 0.0) where the condition is False.

#Determining Data Statistics
df.describe()

df.mean()
df['py-score'].mean()
df.std()
df['py-score'].std()

#Handling Missing Data
# Missing data is very common in data science and machine learning. But never fear! 
# Pandas has very powerful features for working with missing data.
df_ = pd.DataFrame({'x': [1, 2, np.nan, 4]})

df_


#Calculating With Missing Data
# Many Pandas methods omit nan values when performing calculations unless they are 
# explicitly instructed not to:

df_.mean()

df_.mean(skipna=False)

#Filling Missing Data
# Pandas has several options for filling, or replacing, missing values with other values. One of 
# the most convenient methods is .fillna(). You can use it to replace missing values with:

# 1. Specified values
# 2. The values above the missing value
# 3. The values below the missing value


df_.fillna(value=0)
df_.fillna(method='ffill')
df_.fillna(method='bfill')

df_.interpolate()

# You can also use the optional parameter inplace with .fillna(). Doing so will:

# 1. Create and return a new DataFrame when inplace = False
# 2. Modify the existing DataFrame and return None when inplace = True

#Deleting Rows and Columns With Missing Data
# In certain situations, you might want to delete rows or even columns that have missing 
# values. You can do this with .dropna():

df_.dropna()

# In this case, .dropna() simply deletes the row with nan, including its label. It also has the 
# optional parameter inplace, which behaves the same as it does with .fillna() and 
# .interpolate().

#Iterating Over a Pandas DataFrame
# 1. .items() to iterate over columns
# 2. .iteritems() to iterate over columns
# 3. .iterrows() to iterate over rows
# 4. .itertuples() to iterate over rows and get named tuples
for col_label, col in df.iteritems():
    print(col_label, col, sep='\n', end='\n\n')
for row_label, row in df.iterrows():
    print(row_label, row, sep='\n', end='\n\n')
for row in df.itertuples():
    print(row)

f = [1,-3,2,-10,6,-9,1,3]

s = 



