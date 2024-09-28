
'''#1.Write a python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String: 'computer', 'Science'
 Expected Result: ' Scmputer coience '
'''

'''def swap_first_two_characters(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return "both str have at least two chr"
    
    new_str1 = str2[:2] + str1[2:]     #'sc' +'mputer'='scmputer'
    new_str2 = str1[:2] + str2[2:]     #'co'+'ience'='coience'
    
    
    result = new_str2 + ' ' + new_str1
    return result


str1 = 'computer'
str2 = 'Science'



result = swap_first_two_characters(str1, str2)
print(result)  '''

'''2.Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ian', add 'ly'
instead. If the string length of the given string is less than 3, leave it
unchanged.
Sample String : 'CSE'
Expected Result : 'CSEian'
Sample String : 'RBIENT'
Expected Result : 'RBIENTly'''


'''def modify_string(s):
    if len(s) < 3:
        return s
    if s.endswith('ian'):
        return s + 'ly'
    
    return s + 'ing'
    
print(modify_string("ok"))
print(modify_string('CSE'))
print(modify_string("RBIENT"))       
print(modify_string("guardian"))'''


'''3.3. Write a program to add two lists index-wise. Create a new list that contains
the 0th index item from both the list, then the 1st index item, and so on till
the last element. any leftover items will get added at the end of the new list.
Sample
list1 = ["M", "na", "i", "Ge"]
list2 = ["y", "me", "s", "et"]
Expected Result: ['My', 'name', 'is', 'Geet']'''

'''def add_lists_index_wise(list1, list2):

    result = [] 

    max_len = max(len(list1), len(list2))


    for i in range(max_len):
      
      #add the element index wise
        if i < len(list1) and i < len(list2):
            result.append(list1[i] + list2[i])
        elif i<len(list1):
            result.append(list1)
        else:
            result.append(list2)

    return result

# Sample lists
list1 = ["M", "na", "i", "Nik"]
list2 = ["y", "me", "s", "hil"]

# Get the result
result = add_lists_index_wise(list1, list2)
print(result)  '''

#4. Write a Python program to create a calculator class. Include methods for
#basic arithmetic operations
'''
class calculator:
    def add(Self,a,b):
        return a + b
    
    def subtract(self,a,b):
        return a - b

    def multiply(self,a,b):
        return a * b

    def divide(self,a,b):
        if b==0:
            print("cannot divide by zero")
        return a/b    
    
obj=calculator()
print(obj.add(5,3))
print(obj.subtract(5,3))
print(obj.multiply(5,3))
print(obj.divide(5,3))'''

'''import cmath

a=1
b=5
c=6

d=(b**2) - (4*a*c)

sol1=(-b-cmath.sqrt(d)/(2*a))
sol2=(-b-cmath.sqrt(d)/(2*a))

print('the solution of {0} and {1}' .format(sol1,sol2))'''

from datetime import date

d=date(2024,8,12)

'''print("year:",d.year)
print("month:",d.month)
print("day:",d.day)'''

'''today = date.today()
print(today)'''
formatted_date=d.strftime("%A,%B  %d, %Y ")
print("formatted Data:",formatted_date)