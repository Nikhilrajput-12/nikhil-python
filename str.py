"""
string - 1.python string
        2.slicing string = slicing from start,slicing from end
        3.modify string =upper(),lower(,white space remove(split()) , replace())
        4.string concatenate
        5.python escape character
        6.string method = read on w3 school
"""
"""
a="hello world"
print(a[0])    #  h

#loop
for x in a:
    print(x)   

print(len(a)) #11
"""
#check string
"""

txt="this line is used to check the world present is not"
print("world" in txt) #true
print("true" in txt) #false

#if
if "world" in txt:
  print("yes")

print("free" not in txt) #true

if "Free" not in txt:
  print("yes")
  """


#slicing
"""
a="hello world"  #note = last digit not print
print(a[2:5]) #llo

print(a[:5])  #slice from start      #hello
print(a[0:])  #slice from last       #hello world

#negative indexing

print(a[-4:-2])   #or


#modify string
"""
#upper case

a="hEllo"  
print(a.upper())  #HELLO
print(a.lower())   #hello 


#remove whitespace (strip())

b= " hello, world "
print(b.strip())


#replace()

print(b.replace("h","j")) # jello world

#split()

print(b.split())

#string concatenation

x="hello"
y="world"
z=x+y
print(z)

#format string

age = 36
txt="my age is{}"
print(txt.format(age))

#or
txt1 ="my age is{age}"
print(txt)

