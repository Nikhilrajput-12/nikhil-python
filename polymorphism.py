#the ability of something to have or to be displayed in more than one form. 
#or
#The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


#for ex polymorphism in addition operator
#We know that the + operator is used extensively in Python programs. But, it does not have a single usage.

#for datatype + operator is used to arithmetic addition operation
'''n=1
n1=2
print(n+n1)
'''
#for string datatype, + operator is used for concatenate
'''str1="p"
str2="k"
print(str1+str2)'''
# here we see that single operator has been used to carry diiffrent operations for distinct datatype


#function polymorphism len() function
#There are some functions in Python which are compatible to run with multiple data types.
#One such function is the len() function. It can run with many data types in Python. Let's look at some example use cases of the function.

'''print(len(("pro","cro")))#tuple
print(len(["p","y","t"])) #list
print(len({"name":"jonh","add":"nepal"}))'''  #dictionary
#programiz
#Here, we can see that many data types such as string, list, tuple, set, and dictionary can work with the len() function.
#However, we can see that it returns specific information about specific data types.


#CLASS POLYMORPHISM 

'''class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a cat.my name is{self.name},iam {self.age} years old.")

    def sound(self):
        print("meow")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a dog . my name is{self.name}.i am {self.age} years old") 

    def sound(self):
        print(" bow bow")

obj1=cat("kitty",2)
obj2=dog("bruzzo",3)

for animal in (obj1,obj2):
 animal.info()
 animal.sound()'''

#Here, we have created two classes Cat and Dog. They share a similar structure and have the same method names info() and make_sound().

#However, notice that we have not created a common superclass or linked the classes together in any way. 
#Even then, we can pack these two different objects into a tuple and iterate through it using a common animal variable. 
# It is possible due to polymorphism.


#POLYMORPHISM AND INHERITENCE

#Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. 
# We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.
#Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

#METHOD OVERRIDDEN IN POLYMORPHISM
from math import pi

class shape:
    def __init__(self,name):
        self.name=name

    def area(self):
        pass

    def fact(self):
        return " i am a two dimensional shape"
    
    def __str__(self):
        return self.name
    
class square(shape):
    def __init__(self,length):
        super().__init__("square")
        self.length=length

    def area(self):
        return self.length**2
    
    def fact(self):
        return " square have each angle equal to 90 degrees."
    
class circle(shape):
    def __init__(self,radius):
        super().__init__("circle")
        self.radius=radius

    def area(self):
        return pi*self.radius**2
    
a=square(4)
b= circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

#programiz
