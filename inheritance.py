#inheritance allow us to to inherit all teh methods and property from another class
#types #1.single inheritence
       #2.multiple inheitence
       #3.multilevel inheritence 
#parent class from which the child class inherits is known as the superclass(parent or base class)
#child class newly created class that inherit the properties from another class also called derived class

#programiz

'''class animal:
    name=""   #attribute and methods of parent class

    def eat(self):
        print("i can eat")
# inherit from animal class
class dog(animal):

    #new method in subclass
    def display(self):
        #acess name attribute from superclass using self
        print("my name is :",self.name)

#create a object of subclass
labrador=dog()

#acces the superclass attributes and method
labrador.name="tommy"
labrador.eat()

#call subclass
labrador.display()'''


#method overriding
#In the previous example, we see the object of the subclass can access the method of the superclass.
#However, what if the same method is present in both the superclass and subclass?
#In this case, the method in the subclass overrides the method in the superclass. This concept is known as method overriding in Python.

'''class animal():
    name=""

    def eat(self):
     print("i can eat")

class dog(animal):
    #method override
    def eat(self ):
        print("i like to eat")

labrador=dog()


labrador.eat()'''


# the SUPER function 

#Previously we saw that the same method (function) in the subclass overrides the method in the superclass.
#However, if we need to access the superclass method from the subclass, we use the super() function. For example,

'''class animal:
   name= ""

   def eat(self):
      print("i can eat")

class dog(animal):  # inherit
   #override eat() method
    def eat(self):
       
       #call the eat() method of the superclass using super()
       super().eat()

       print("i like the bones")

labrador=dog()

labrador.eat()
'''
#multiple inheritence
# a class derived from more then one superclass is called multiple inheritence

'''class s1:    #1 superclass
   def f1(self):
      print("first superclass")

class s2:    #2 superclass
   def f2(self):
      print("second superclass")

class subclass(s1,s2):
   pass

obj1=subclass()   #create the obj of subclass to access both classes at one time
#or you also create the object of superclass to acces the classes
obj1.f1()
obj1.f2()'''


#MULTILEVEL INHERITENCE
#in python,not only can we derive a class from the superclass but you can also derive a class from the derived class.this form of inheritence is known as multilevel inheirtence

'''class superclass:
   def f1(self):
      print("this is  a superclass")

class subclass1(superclass):
   def f2(self):
      print("subclass derived from superclasas")

class subclass2(subclass1):
   def f3(self):
      print("this is derived from subclass1")

obj=subclass2()

obj.f1()
obj.f2()
obj.f3()'''

# METHOD RESOLUTION ORDER (MRO)
# if two superclassess have the same method(function) name and the derived class calls that method ,python uses the MRO to search the right method to call

class superclass:
    def f1(self):
        print("superclass 1")

class superclass1:
    def f1(self):
        print("superclass 2")

class subclass(superclass,superclass1):
    pass

obj=subclass()

obj.f1()
#Here, SuperClass1 and SuperClass2 both of these classes define a method info().

#So when info() is called using the d1 object of the Derived class, Python uses the MRO to determine which method to call.

#In this case, the MRO specifies that methods should be inherited from the leftmost superclass