#exception syntax
# try:
#     # do stuff
# except Exception:
#      # handle exceptions



raise IndexError("Just kidding")

# first argument given to exception is considered as message 

#syntax for exception handler
# try:
#  body
# except exception_type1 as var1:
#  exception_code1
# except exception_type2 as var2:
#  exception_code2
#  .
#  .
#  .
# except:
#  default_exception_code
# else:
#  else_body
# finally:
#  finally_body


# The else clause of a try statement is optional and is rarely used. It’s executed if
# and only if the body of the try statement executes without throwing any errors.

# The finally clause of a try statement is also optional and executes after the try,
# except, and else sections have executed. If an exception is raised in the try block
# and isn’t handled by any of the except blocks, that exception is reraised after the
# finally block executes. Because the finally block always executes, it gives you a
# chance to include code to clean up after any exception handling by closing files, resetting variables, and so on.


# Defining new exceptions
# You can easily define your own exception. The following two lines will do this for you:


try:
    z = [1]
    z[0]
    5/0
    j = 0
except Exception as w:    
    print("divide by by zero is not possible")
except IndexError as a:
    print("i am handling index error")
else:
    print("code executed without errors")
finally:
    print("finally i am doing this")




class MyError(Exception):
    pass

try:
    d = 3
    raise MyError("Some information about what went wrong",d)
except MyError as error:
    print("Situation:", error)
    print(error.args[1])


# If you raise your exception with multiple arguments, these will be delivered to your
# handler as a tuple, which you can access through the args variable of the error:


#The exception inheritance hierarchy
try:
    body
except Exception as error:
    exception code
except IndexError as error:
    exception code

#mangglesh solution for assignment
#assignment question please use the following string and make the next string as upper case after period? and give back the result

a = """We talked before about the difference between evaluating a Python expression interactively and printing the result of the same expression using the print function.
Although the same string is involved, the two operations can produce screen outputs
that look different. a string that is evaluated at the top level of an interactive Python
session will be shown with all of its special characters as octal escape sequences, which
makes clear what is in the string. meanwhile, the print function passes the string
directly to the terminal program, which may interpret special characters in special
ways. for example, here’s what happens with a string consisting of an a followed by a
newline, a tab, and a b"""

bag_or_word = a.split()
for word_number in range(len(bag_or_word)):
    if bag_or_word[word_number][-1] == ".":
        bag_or_word[word_number+1] = bag_or_word[word_number+1].capitalize()
" ".join(bag_or_word)

