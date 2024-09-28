# An exception is an unexpected event that occurs during program execution. For example,

'divide_by_zero = 7/0'
#the above code causes an exception as it is not possible to divide a number by 0.
#Here, while trying to divide 7 / 0, the program throws a system exception ZeroDivisionError

#Python Built-in Exceptions
#Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.
#We can view all the built-in exceptions using the built-in local() function as follows:
'''print(dir(locals()['__builtins__']))'''

#PYTHON TRY ...EXCEPT BLOCK
#THE TRY ..EXCEPT BLOCK IS USED TO HANDLE EXCEPTION IN PYTHON.

#SYNTAX

#try:
    #code that may cause exception
#except:
    #code to run when exception occurs


'''try:
    numerator=10
    denominator=0

    result=numerator/denominator

    print(result)

except:
    print("errors:denominator cannot be 0")'''


#CATCHING SPECIFIC  EXCEPTIONS IN PYTHON
#For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently.

#The argument type of each except block indicates the type of exception that can be handled by it. For example,

'''try:

    even_number=[2,4,6,8]
    print(even_number[5])

except ZeroDivisionError:
    print("denominator cannot br zero")

except IndexError:
    print("index out of bound")'''


#Here, we are trying to access a value to the index 5. Hence, IndexError exception occurs.

#When the IndexError exception occurs in the try block,

#The ZeroDivisionError exception is skipped.
#The set of code inside the IndexError exception is executed.

#PYTHON TRY WITH ELSE CLAUSE
#In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.
#For these cases, you can use the optional else keyword with the try statement.

'''try:
    num=int(input("enter the numbers:"))
    assert num % 2 == 0
except:
    print("not an even number !")
else:
    reciprocal = 1 /num
    print(reciprocal)'''

 #   Note: Exceptions in the else clause are not handled by the preceding except clauses.


 #PYHTON TRY ...FINALLY

 #in python the finally block is always executed no matter whether there is an exception or not

 #the finally block is optional  and for each try block there cab be only one finally block

try:
    numerator=10
    denominator=0

    result = numerator/denominator

    print(result)
except:
    print("error : Denominator cannot be 0.")

finally:
    print("this is finally block.")
