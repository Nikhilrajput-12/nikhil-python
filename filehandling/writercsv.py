import csv
#csv file have pipe delimeter

data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)
# output

#     SN|Name|Contribution
# 1|Linus Torvalds|Linux Kernel
# 2|Tim Berners-Lee|World Wide Web
# 3|Guido van Rossum|Python Programming


# csv file with quotes
#diffrent types of inbuilt quotes are given we chek on net

data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,delimiter=';')
    writer.writerows(data_list)

#note:read this file on reading file

    #output
'''['SN;"Name";"Contribution"']
['1;"Linus Torvalds";"Linux Kernel"']
['2;"Tim Berners-Lee";"World Wide Web"']
['3;"Guido van Rossum";"Python Programming"']'''