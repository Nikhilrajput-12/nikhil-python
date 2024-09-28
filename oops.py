#CLASSES AND OBJECTS
#variables inside classes are called attributes

'''class bike:
    name=""      # attributes
    gear=0

bike1=bike()     #create a object

bike1.name="kawasaki"    # assign the new values to the attributes by using object
bike1.gear=11

print(f"Name : {bike1.name}, Gear :{bike1.gear}")'''



#multiple objects

'''class emp:
    empid=0

emp1=emp()
emp2=emp()

emp1.empid=1001

print("id :",emp1.empid)

emp2.empid=1002

print("id : ",emp2.empid)'''

#__init_()Function  'constructor' intialise the value
#w3
#note: the __init__() function is called automatically every time the class being used to create a new object
#Here, __init__() is the constructor function that is called whenever a new object of that class is instantiated.
'''class person:
    def __init__(self,name,age):  # constructor function
        self.name=name
        self.age=age
p1=person("jonh",34)

print(p1.name)
print(p1.age)'''

# the __str__()function
#the__str__() function control the what should be returned when the class object is represented as a string

#WITHOUT __str__fun()
'''class person0:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person0("jonh",34)
print(p1)'''

#with __str__fun()

'''class person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p2=person1("nik",26)
print(p2)'''
    
#object method 
#w3

'''class p:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print(f"hello my name is {self.name} and age {self.age} ")
    
p3=p("k",56)
p3.myfun()'''


#modify object properties

'''class p:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print(f"hello my name is {self.name} and age {self.age} ")
    
p3=p("k",56)
p3.age = 40 # modify 
p3.myfun()'''


#Delete object properties
'''class p:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print(f"hello my name is {self.name} and age {self.age} ")
    
p3=p("k",56)
p3.age = 40 
del p3.age     #delete object properties
p3.myfun()'''

#delete object
'''class p:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print(f"hello my name is {self.name} and age {self.age} ")
    
p3=p("k",56)
del p3    #del object
p3.myfun()
'''

#pass
class person:
    pass

class room:
    length=0.0
    breadth=0.0

    def claculate(self):
        print("area of room is =",self.length*self.breadth)
    
study_room=room()

study_room.length=42.3
study_room.breadth=89.3

study_room.claculate()