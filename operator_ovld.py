#PYTHON OVERLOADING
#READ ON PROGRAMIZ

class point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "{0},{1}".format(self.x,self.y)

    def __add__(self,other):
        x=self.x + other.x
        y= self.y + other.y

        return point(x,y)
    
p1=point(1,2)
p2=point(2,3)

print(p1+p2)


#OVERLOADING COMPARISON OPERATORS
#Python does not limit operator overloading to arithmetic operators only.
#we can overload comparison operator as well.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #overload < operator
    def __lt__(self,other):
        return self.age < other.age
    
p1=person("alice",20)
p2=person("bob",30)

print(p1<p2)
print(p2<p1)