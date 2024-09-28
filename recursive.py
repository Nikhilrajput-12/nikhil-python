#Recurive function can call itself

#Advantages of Recursion

#1.Recursive functions make the code look clean and elegant.
#2.A complex task can be broken down into simpler sub-problems using recursion.
#3.Sequence generation is easier with recursion than using some nested iteration.

#Disadvantages of Recursion
#1.Sometimes the logic behind recursion is hard to follow through.
#2.Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
#3.Recursive functions are hard to debug.


def factorial(x):
 


 if x==1:
        return 1 
 else:
       return(x * factorial(x-1))

     
x=int(input("enter the number:"))
print(factorial(x))

#Find Sum of Natural Numbers Using Recursion

def sum_natural(n):
     if n<0:
          return n
     else:
          return n + sum_natural(n-1)
     
n=int(input("enter the numbers:"))
print(sum_natural(n))


#Display Fibonacci Sequence Using Recursion

def fibbonaci(n):
     if n<=0:
          return 0
     elif n==1:
          return 1
     else:
          return fibbonaci(n-1)+fibbonaci(n-2)
     
def display(num):
     for i in range(num):
          print(fibbonaci(i),end=" ")
     
num=int(input("enter the number:"))
print(display(num))