#GLOBAL
'''
x ="awesome"
def myfun():
    print("python is " +x)

myfun()
'''


#LOCAL
'''''
x="awesome"      #global

def myfun():
    x="fantastic"      #local

    print("python is" +x)
myfun()

print("python is " +x)
'''

#GLOBAL KEYWORD
# to create a global varible inside the function we use global keyword

x="awesome"
def myfun():


 global x

x="fantastic"
myfun()
print("python is " +x)