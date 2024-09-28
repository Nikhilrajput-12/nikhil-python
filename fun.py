'''def greet():  # func
 print("hello world")

greet()  #call


def my_fun(fname):  #arguments
 print(fname + " hello")

my_fun("ramu ")  #numbers of argument
def my_fun1(fname,lname):
  print(fname + " " + lname)

my_fun1("hi","kida")

5 types Arguments in Python to Know
1.default arguments
2.keyword arguments
3.positional arguments
4.arbitrary positional arguments
5.arbitrary keyword arguments

#1.arbbitary arguments, *args

#if you dont know how many argumnets passed into your function
def my_function(*kids):
 print("the youngest child is " +kids[2])

my_function("evil","tomas","raku")'''

'''
#2.Keyword Argument

#you can also use the arguments with the key = value syntax
#this way the order arguments does not matter

def my_fun(child1="hlo", child2="h",child3="g"):

    print("the youngest child is ",child1)
my_fun()


#3.Arbitary keyword argument, **kwargs

# if you dont know how many keywords arguments that will be passed into your function,Add ** before the parameter pass
#this way the function will receive a dictionary of arguments, and can access the items

def my_fun1(**kid):
    print("his name is",kid["fname"])
my_fun1(fname="tobias",lname="ho")

#Default parameter value
#if we call the function without argument,it uses the default value:

def my_function(country="nor"):
    
    print("i am from",country)
my_function("sweden")
my_function("india")
my_function()
my_function("brazil")'''

'''#4.Passing a list as an Argument

#you can send any data types of argument to a function (str,num,list,dictetc),and it will be treated as same data type inside the function
#ex if you send a list as an argument it will b still be a list when it reaches the function

def my_fun(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_fun(fruits)

#return value

def my_fun1(x):
    return 5 * x
print(my_fun1(3))
print(my_fun1(4))
'''
'''#Pass statement

#function definitions cannot be empty,
#but if you for some reason have a function definition with no content,
#put in the pass statement to avoid getting an error.

def myfunction():
    pass
'''

#5.postional aguments

def my_fun(x,/):
  print(x)
my_fun(4) #4

#6 keyword-only arguments
# to specify that a function can have only keyword arguments,add#,before the argument

def my_fun1(*,x):
  print(x)
# my_fun1(3)   error
my_fun1(x=3)

#7 combine postional-only and keyword only

def my_function(a,b,/,*,c,d):
  print(a+b+c+d)

my_function(5,6,c=7,d=8)
