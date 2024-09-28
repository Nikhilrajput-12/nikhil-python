import csv

'''with open("/Users/nikhilsingh/Desktop/python/file1.csv",'r') as file:
    # because my file is in other directory so i can acces the file using thepath
    read=csv.reader(file)
    for row in read:
        print(row)


'''

# CSV files with Custom Delimeters

# By default, a comma is used as a delimiter in a CSV file. However, some CSV files can use delimiters other than a comma. Few popular ones are | and \t.
# Suppose the innovators.csv file in Example 1 was using tab as a delimiter. To read the file, we can pass an additional delimiter parameter to the csv.reader() function.

'''with open('f.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
        print(row)'''

#READ CSV files with initial spaces
'''with open('f.csv','r') as file:
    read=csv.reader(file,skipinitialspace=True)
    for row in read:
        print(row)'''

#read csv with quotes

'''with open('f.csv','r') as file:
    read=csv.reader(file, quoting=csv.QUOTE_ALL,skipinitialspace=True)
    for row in read:
        print(row)
'''
#read baki on programiz
'''with open('writercsv.py','w') as file:
   file.write(" i am good")
   file.write("hello ")
   '''

#read a writercsv file
with open('innovators.csv','r') as file:
    read =csv.reader(file)

    for row in read:
        print(row)

