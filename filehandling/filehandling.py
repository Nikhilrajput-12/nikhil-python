import os
'''import os

os.chdir('/Users/nikhilsingh/desktop/python')  #change directory

print(os.getcwd())  #current working directory

print(os.listdir ()) #list directory'''
# change directory
'''import os

os.chdir('/Users/nikhilsingh/Desktop/python')'''

# MAKING A NEW DIRECTORY IN PYTHON
#MKDIR()

'''os.mkdir("nikhil")


print(os.listdir())'''

#Renaming a directory

'''import os

#os.mkdir('test')
print(os.listdir())
['test']

os.rename('test','new_one')
print(os.listdir())
'''
#create file

'''with open("file.txt",'w') as file:
    file.write("this is file")
'''

#remove a file or directory

'''os.rmdir('new_one')  #remove a directory
os.remove("myfile.txt")''' #remove a file



#In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module. For example,
'''import shutil

shutil.rmtree("my")'''


#basic file operation
#A file is a named location used for storing data. For example, main.py is a file that is always used to store Python code.

#1. open()
#in python we need to open a file to perform any function first open the file
'''file=open("f.txt")''' #open the file 

#2.write()fun
'''file1=open("f.txt",'w') # open the file
file1.write("program is fun \n")
file1.write("good")'''

#3.reading a file  'read()'
'''fil=open('f.txt')

read=fil.read()
print(read)'''

#4.Closing a file in python
#When we are done performing operations on the file, we need to close the file properly. We use the close()
#  function to close a file in Python. For example,

'''fil = open('f.txt') #open

read=fil.read() # read
print(read)

fil.close()'''  #close the file
 #Note: Closing a file will free up the resources that are tied to the file. Hence, it is a good programming practice to always close the file.


#opening a file using WITH...OPEN

'''with open('f.txt','r') as f:
    read=f.read()
    print(read)'''

#Here, with...open automatically closes the file, so we don't have to use the close() function.
#Note: Since we don't have to worry about closing the file, make a habit of using the with...open syntax.
#Note: Make a habit of using the with...open syntax while working with files so you don't have to worry about closing the file.


'''## open a file in default mode (read and text)
file1 = open("f.txt")      # equivalent to open("test.txt", "rt")

# open a file in write and text mode 
file1 = open("f.txt",'w')  

# open a file in read, write and binary mode
file1 = open("f.txt",'+b') '''

#using full path read and write file
'''file_path = "/Users/nikhilsingh/Desktop/python/f.txt"
file1 = open(file_path)

read=file1.read()
print(read)'''

'''file_path="/Users/nikhilsingh/Desktop/python"
file=open('file_path','w')

file.write("i am good \n ")
file.write("sure")

file.close()'''

#or
'''file_path = "/Users/nikhilsingh/Desktop/python/f.txt"'''

# Open the file in write mode using a context manager
'''with open(file_path, 'w') as file:
    file.write("i am good \n")
    file.write("sure")'''

#exception handling in files 

#If an exception occurs while working with a file, the code exists without closing the file. Hence, it's a good practice to use the try...finally block.

try:
    file1=open("f.txt","r")
    read=file1.read()
    print(read)

finally:
    file1.close()

#Here, the finally block is always executed, so we have kept the close() function inside it. This ensures that the file will always be closed.
#Note: Make a habit of using the with...open syntax while working with files so you don't have to worry about closing the file.
# There are various methods available with a file object. Some of them have been used in the above examples.

'''Here is the complete list of methods in text mode with a brief description:

Method  	Description
close()	    Closes an opened file
read(n)	    Reads the file content
seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end)
tell()           Returns an integer that represents the current position of the file's object
write(s)	            Writes a string to the file 
writelines(lines)   	Writes a list of lines to the file
'''