#PYTHON CSV:READ AND WRITE CSV FILES
#CSV:comma separated value

#working with csv files in python

#Python provides a dedicated csv module to work with csv files. The module includes various methods to perform different operations.


import csv

#the csv module provides the csv.writer() function to a csv file.
'''with open("file1.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['sn','movie','spiderman'])
    writer.writerow([1,'lord','frodo'])
    writer.writerow([2,'harry','potter'])'''

"in this example we have created a CSV file"

#the csv module provides the ''csv.reader()'' function to read a csv file.

'''with open('file1.csv','r') as file:
    reader=csv.reader(file)

#without loop
data=list(reader)'
print(data)'''

#or (csv.reader)
'''with open("file1.csv",'r') as file:
   read=csv.reader(file)

    for data in read:
      print(data)'''

# csv.dictreader
# print each row as a dictionary

with open("file1.csv",'r') as file:
    csv_file=csv.DictReader(file)
    for row in csv_file:
        print(row)