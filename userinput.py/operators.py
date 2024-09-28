#types of operators 

#1.Arithmetic opt(+,-,*, /(division), //(floor dvs),%, **(power))

#2.Assignment operators(=,+=,-=,*=,/=,%=,**=)
#additonal asign (briefly on copy)
#ex
'''
a=5
b=10
a+=b   #a=a+b
print(a)  #15
'''


#3.Comparison opertor(==,!=,>,<,>=,<=)
'''
a=2
b=3
print(a==b) #false
print(a<b) #true
'''


#4. Logical operator(and,or,not)
#AND
''''
a=7
b=6
print((a>8)and(b>=6))  '''# both conditon is true
#print(true and true)=true
#print(true and false) =false

#OR
'''
a=5
b=6
print((a>b)or(b>a))   #one conditon is true
#print(true and false) =true
'''
#not
'''
a=5
b=4
print(not(b>a))  # true if the conditon is false
'''

#5. identical operators(is,is not)
#ex
x1=5
y1=5
x2="hello"
y2="hello"
print(x1 is y1) # true
print(x2 is not y2) # false

#6. Membership operator(in, not in)   
# ( this is used for check the sequence)
# ( mostly used in dictionary for presence of key not the value)
#ex
x="hello world"
y={1:"a",2:"b"}

print("h" in x) # true
print("i" in x) #false
print("hello" in x)

print(1 in y) #true
print('a' in y) #false   (becase python case senstive here (a) is value in dictinary we acces only key herekey is 1,2)



