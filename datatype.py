'''
a =5 
b="hello"
c=20.5
d=1j                                #complex
e=["apple","banana"," chery"]       #list
f=("apple","banana","cherry")      #tuple
g=range(6)
h=dict({"name":"john","age":35})         #dictionary
i={"apple","banana","cherry"}       #set
j=frozenset(["apple","banana","cherry"]) #frozenset

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
'''
#2. COMPLEX NUMBER
'''
x = 3+5j
print (x)
'''
#3. TYPE CONVERSION
'''
x=5
y=2.4
z=1j

a=float(x)
b=int(y)
c=complex(z)

print(a)
print(b)
print(c)
'''

#4.RANDOM NUMBER
'''
import random

print(random.randrange(1,1100)) 
'''
#5. LIST 
'''''
x=["SWIFT","DESIRE","MARUTI"]

print(x[2])
'''''

#6. TUPLE
'''''
x=("swift","desire","maruti")
print(type(x))
'''''
#7. string
'''''
x=str("hi")
print(x)
'''''

#8. set
'''''
x={"swift","maruti","desire"}
print(type(x))
'''''


#dictionary
'''
capital_city={'nepal':"kathmandu" ,"india":"delhi","italy":"rome"}
print(capital_city)

print(capital_city['nepal'])  #acces the key they give the value
print(capital_city['india'])
'''''
#concatinate string and use the 'end=()' paramater to joint the two lines

print("program" + " is good ",end=(""))
print("thnks")

#separate parameter use  'sep=()'

print("new year",2020,"see you",sep=(','))

#output formatting   'str.format()'

x="hi"
y="ki"
print("the value of x is {} and y is {}".format(x,y))