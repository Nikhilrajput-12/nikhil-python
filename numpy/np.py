
import numpy as np
#numpy array class is called  'ndarray'  also known as alias array.
# Note that numpy.array is not the same as the Standard Python Library class array.array, 
# which only handles one-dimensional arrays and offers less functionality. 

#The more important attributes of an ndarray object are:

''' 1.ndarray.ndim
the number of axes (dimensions) of the array.

2.ndarray.shape
the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.

3.ndarray.size
the total number of elements of the array. This is equal to the product of the elements of shape.

4.ndarray.dtype
an object describing the type of the elements in the array. One can create or specify dtypes using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

5.ndarray.itemsize
the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

6.ndarray.data
the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
'''

'''import numpy as np
a=np.arange(15).reshape(3,5)

print(a) 
print(a.shape)       #(3,5)
print(a.ndim)        #2
print(a.size)        #15
print(a.dtype)       #int64
print(a.itemsize)    #8byte 
print(a.data)  
'''


# ARRAY CREATION
# There are several ways to create arrays

'''
a=np.array([2,3,4])
print(a)    
print(a.dtype)

b=np.array([2.1,3.3,4.2])
print(b)
'''
# array transforms sequences of sequences into two-dimensional arrays,
# sequences of sequences of sequences into three-dimensional arrays, and so on.
 
'''a=np.array(((1,2,3,4),(2,3,4,5)))
print(a)
'''
# The type of the array can also be explicitly specified at creation time:

'''a=np.array(([1,2],[2,1],[2,1]),dtype=complex)
print(a)'''

# Often, the elements of an array are originally unknown, but its size is known.
#  Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.

'''1.(zeros) creates an array full of zeros, the function
2.(ones) creates an array full of ones, 
and the function 3.(empty) creates an array whose initial content is random and depends on the state of the memory. 
By default, the dtype of the created array is (float64), but it can be specified via the key word argument dtype.'''

'''a=np.zeros((3,4))
print(a)

b=np.ones((2,3))
print(b)

c=np.empty((2,2))
print(c)
'''
#arange fun
# To create sequences of numbers, 
# NumPy provides the arange function 
# which is analogous to the Python built-in range, but returns an array.


'''a=np.arange(10,30,4)    #arange in order diff 4
print(a) '''#[10 14 18 22 26]

#also accept the float


# When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, 
# due to the finite floating point precision. 
# For this reason, it is usually better to use the function linspace that receives as an argument the number of elements that we want, 
# instead of the step:

#linspace

'''from numpy import pi

a=np.linspace(0,2,9) 
print(a) #9 numbers from 0to 2

b=np.linspace(0,2*pi,10)
c=np.sin(b)
print(c)
'''


#2.BASIC OPERATIONS

'''a = np.array([20,30,40,50])
print(a)
b = np.arange(4)

print(b) #[0 1 2 3]

c = a-b
print(c) #[20 29 38 47]

print(b**2) #[0 1 4 9]

print(10* np.sin(a)) #[ 9.12945251 -9.88031624  7.4511316  -2.62374854]

print(a < 35) # [ True  True False False]'''


# Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays.
#  The matrix product can be performed using the @ operator (in python >=3.5) or the dot function or method:
'''
a=np.array(([1,2],
            [2,0]))
b=np.array(([2,0],
            [3,0]))

c=a*b    #elementwise product
print(c) 

d=a@b
print(d) #matrices product

e=a.dot(b)
print(e) #another matrix method'''

# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

'''a =np.random.default_rng(1)  
b=np.ones((2,3),dtype=int)
c=a.random((2,3))  #filled with random floating numbers
b *= 3    #no of ones multiply by 3

print(b)
c += b     #b di value + krke c ch pani
print(c)

b +=c  # this show error because b is a int type array or c is a float type array bydefault
       #  so overcome this we need to change b float to int
b +=c.astype(int)       
print(b)'''

# When operating with arrays of different types, 
# the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).
from numpy import pi

'''a=np.ones(3, dtype=np.int32)
print(a)                  #[1 1 1]
b=np.linspace(0,pi,3)     
print(b)                    # [0.         1.57079633 3.14159265]
print(b.dtype.name)

c=a+b
print(c)                  # [1.         2.57079633 4.14159265]

d=np.exp(c*1j)           #[ 0.54030231+0.84147098j -0.84147098+0.54030231j -0.54030231-0.84147098j]
print(d)
print(d.dtype)
'''
# Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class.
'''rg=np.random.default_rng(1)
a =rg.random((2,3))
print("Array: \n",a)

a =np.arange(10,20,2)
print(a)

print("sum :",a.sum()) #sum of all elements in array
print("min:",a.min())   #print min value 
print("max:",a.max())'''   #print max value


# By default, these operations apply to the array as though it were a list of numbers, regardless of its shape.
#  However, by specifying the axis parameter you can apply an operation along the specified axis of an array:

'''a=np.arange(12).reshape(3,4)
print(a)

print(a.sum(axis=0))  #sum of each column
print(a.sum(axis=1)) #  sum of each row
print(a.min(axis=1))  #min of each row
print(a.cumsum(axis=1)) ''' #cumulative sum along each row

#UNIVERSAL FUNCTION

# NumPy provides familiar mathematical functions such as sin, cos, and exp. 
# In NumPy, these are called “universal functions” (ufunc). 
# Within NumPy, these functions operate elementwise on an array, producing an array as output.

'''a = np.arange(3)
print(a)  #[0 1 2]
print(np.exp(a))    #expotetial       [1.         2.71828183 7.3890561 ]
print(np.sqrt(a))   #sqrt    #[0.         1.         1.41421356]

b=np.array([2.,-1.,4.])
print(b)

print(np.add(a,b))  '''  #[2. 0. 6.]


# INDEXING, SLICING AND ITERATING

# one dimensional arrays can be indexed,sliced and iterated
# over,much like lists and other python sequences.

'''a =np.arange(10)**3
print(a)       #[  0   1   8  27  64 125 216 343 512 729]
print(a[2])    #8
print(a[2:5])  #[ 8 27 64]
a[0:6:2]=1000   #modifies every 2nd element from the start to index 6 (not including index 6), 
#so the elements at indices 0, 2, and 4 are set to 100.
print(a)   #1000   1 1000  27 1000 125 216 343 512 729]
print(a[::-1])  #reversed a



for i in a:
    print(i**(1/3))     #a=#100   1 100  27 100 125 216 343 512 729]    cuberoot this term
    '''
 

# ...Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:
'''def f(x,y):
    return 10 * x + y

b = np.fromfunction(f,(5,4), dtype=int)     #5*4 array create
print(b[2,3])     #parameter

print(b[0:5,1])  #For each row x, the value in column 1 is computed as 10 * x + 1.
print(b[:,1])   # equivalent to the previous example

print(b[1:3,:]) ''' #Given the function f(x, y) = 10 * x + y used to create b, let’s compute the values for the slice b[1:3, :].

# When fewer indices are provided than the number of axes, the missing indices are considered complete slices:
# print(b[-1])

# The expression within brackets in b[i] is treated as an i followed by as many instances of : as needed to represent the remaining axes. NumPy also allows you to write this using dots as b[i, ...].
# The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is an array with 5 axes, then
# x[1, 2, ...] is equivalent to x[1, 2, :, :, :],
# x[..., 3] to x[:, :, :, :, 3] and

'''a = np.array([[[0,1,2],
               [10,20,30]],
               [[100,101,102],
               [110,112,113]]])
print(a.shape)    #The shape of the array a is (2, 2, 3).

# This means:

# The array has 2 blocks (outermost dimension),
# Each block contains 2 rows (second dimension),
# Each row contains 3 elements (innermost dimension).


print(a[1,...])  # same as a[1, :, :] or a[1]

print(a[...,2])  #The expression a[..., 2] selects the element at index 2 from the last dimension of the array, across all other dimensions

# Iterating over multidimensional arrays is done with respect to the first axis:
for row in a:   #simple iterate array
    print(row)

for row in a.flat:  # iterate single element
    print(row)
'''

#...Shape manipulation

# changing the shape of an array

'''rg = np.random.default_rng()
a=np.floor(10 * rg.random((3,4)))   #rg.random((3, 4)) generates random values between 0 and 1.
print(a)
print(a.shape)

print(a.ravel())   # returns the array, flattened

print(a.reshape(6,2))   # returns the array with a modified shape

print(a.T)
print(a.T.shape)
print(a.shape)

# The reshape function returns its argument with a modified shape, whereas the ndarray.resize method modifies the array itself:
print(a)
# a.resize(2,5)
# print(a)

# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:


a.reshape(3,-1)   ## NumPy will calculate the number of columns
print(a) '''

#..stacking together diffrent arrays

''''rg = np.random.default_rng(1)

a=np.floor(10 * rg.random((2,2)))   #floor cannot show the after point value
# print(a)

b = np.floor(10*rg.random((2,2)))
# print(b)

v=np.vstack((a,b))
print(v)

h=np.hstack((a,b))
print(h)


from numpy import newaxis

c=np.column_stack((a,b)) #with 2d array
print(c)

a1=np.array([4,3])
b1=np.array([3,8])

c1=np.column_stack((a1,b1))  #return 2d array
print(c1)

d1=np.hstack((a,b))
print(d1)

d2=a1[:, newaxis]
print(d2)  # [[4]
            # [3]]

d2=np.column_stack((a1[:, newaxis], b1[:, newaxis]))
print(d2)

d3=np.hstack((a1[:, newaxis], b1[:, newaxis]))
print(d3)

r=np.r_[1:4,0,4]
print(r)'''


#...splitting one array into several smaller ones
#using hsplit

'''import numpy as np

rg =np.random.default_rng(1)

a=np.floor(10 * rg.random((2,12)))
print(a)

b=np.hsplit(a,3)  #split a into 3
print(b) 

#split a after the third and the fourth column

c=np.hsplit(a,(3,4))
print(c)'''

# Copies and Views
# When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

# NO COPY ATALL
# simple assignment make no copy of objects or their data.

'''a =np.array([[0,1,2,3],
           [4,5,6,7],
             [8,9,10,11]])
b= a     # no new object is created
if b is a:  # a and b are two names for the same ndarray object
    print(True)
else:
    print(False)

def f(x):
    print(id(x))

f(a)   #call the function
print(id(a))

#view or shallow copy
# Different array objects can share the same data. The view method creates a new array object that looks at the same data.


c =a.view()
if c is a:
    print(True)
else:
    print(False)

if c.base is a:   # c is a view of the data owned by a
    print(True)

if c.flags.owndata:    #The .flags.owndata attribute indicates whether the array owns its data. Since c is a view and doesn't own the underlying data (it's shared with a), this returns False.
    print(True)
else:
    print(False)

c=c.reshape((2,6))   # a's shape doesn't change
print(c)   
print(a.shape)

c[0,4] =1234  # a's data changes
print(a)

#slicing an array returns a view of it:

s=a[:,1:3]  #This creates a view of a, extracting a subarray s that consists of columns 1 and 2 (index positions 1:3) from all rows:
#Note that s is a view of a, not a copy. Any changes made to s will affect a.


s[:]= 10  #s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
# This line assigns the value 10 to all elements of s. Since s is a view of a, the corresponding elements in a are also updated:

# This line assigns the value 10 to all elements of s. Since s is a view of a, the corresponding elements in a are also updated:
print(a)  #After modifying s, printing a shows the updated array, where columns 1 and 2 have been replaced with 10:
'''

#DEEP COPY
# The copy method makes a complete copy of the array and its data.

'''a = np.array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])

d =a.copy() # a new array object with new data is created

if d is a:        # d id indepent it will not effect a so d is not a
    print(True)

else:
    print(False)

if d.base is a:    # d doesn't share anything with a
    print(True)
else:
    print(False)

d[0,0]=9999   #when you modify it will effect on d because d is an independent
print(d)   #d output 
print(a)    # a has no effect

a=np.arange(int(1e8))
b=a[:100].copy()   #a[:100] creates a slice of the first 100 elements of a. This slice is a view of a, meaning that the data is shared between a and the slice.
#However, calling .copy() on this slice creates a deep copy, so b is a new array containing the first 100 elements of a. It does not share memory with a.

print(a)
print(b)

del a   #del a
print(a)'''


#ADVANCED INDEXING AND INDEX TRICKS

#INDEXING WITH ARRAYS OG INDICES
a=np.arange(12)**2    #the first 12 square numbers
'''i=np.array([1,1,3,8,5])
print(a)
print(a[i])   #prints elements from 'a' at indices specified in 'i'


j=np.array([[3,4],[9,7]])   
print(j)
print(a[j]) ''' #the same shape as `j`

#When the indexed array a is multidimensional, a single array of indices refers to the first dimension of a. 
# The following example shows this behavior by converting an image of labels into a color image using a palette.

import numpy as np
import matplotlib.pyplot as plt

'''# Define the palette (RGB values for colors)
palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white

# Define the image array with indices corresponding to the palette
image = np.array([[0, 1, 2, 0],  # first row
                  [0, 3, 4, 0]]) # second row

# Map the image to the palette (the resulting array will be in RGB format)
color_image = palette[image]

# Plot the image using matplotlib
plt.imshow(color_image)
plt.axis('off')  # Turn off the axes for better visualization
plt.show()'''


# We can also give indexes for more than one dimension. The arrays of indices for each dimension must have the same shape.

'''a = np.arange(12).reshape(3,4)
print(a)

i=np.array([[0,1],
            [1,2]])
j=([[2,1],  # indices for the first dim of `a`
    [3,3]])  # indices for the second dim

print(a[i,j])   #The first pair of indices is (i[0, 0], j[0, 0]) → (0, 2) → a[0, 2] = 2.
# The second pair is (i[0, 1], j[0, 1]) → (1, 1) → a[1, 1] = 5.
# The third pair is (i[1, 0], j[1, 0]) → (1, 3) → a[1, 3] = 7.
# The fourth pair is (i[1, 1], j[1, 1]) → (2, 3) → a[2, 3] = 11.


print(a[i,2])   #The first pair is i[0, 0] = 0, so a[0, 2] = 2.
# The second pair is i[0, 1] = 1, so a[1, 2] = 6.
# The third pair is i[1, 0] = 1, so a[1, 2] = 6.
# The fourth pair is i[1, 1] = 2, so a[2, 2] = 10.

print(a[:,j])  #Element Selection for a[:, j]:
# For row 0: j = [[2, 1], [3, 3]]

# a[0, 2] = 2, a[0, 1] = 1
# a[0, 3] = 3, a[0, 3] = 3
# For row 1: j = [[2, 1], [3, 3]]

# a[1, 2] = 6, a[1, 1] = 5
# a[1, 3] = 7, a[1, 3] = 7
# For row 2: j = [[2, 1], [3, 3]]

# a[2, 2] = 10, a[2, 1] = 9
# a[2, 3] = 11, a[2, 3] = 11

# In Python, arr[i, j] is exactly the same as arr[(i, j)]—so we can put i and j in a tuple and then do the indexing with that.

l=(i,j)
#equivalent to a[i,j]
print(a[l])

s=np.array([i,j])  # not what we want
# print(a[s])    #error

print(a[tuple(s)])'''



# Another common use of indexing with arrays is the search of the maximum value of time-dependent series:


'''
time  = np.linspace(20,145,5)  #time scale
data = np.sin(np.arange(20)).reshape(5,4)  #4 time-dependent series

print(time)#The time array is generated using the np.linspace(20, 145, 5) function. Let's break this down:

# Syntax of np.linspace(start, stop, num):
# start: The starting value of the sequence (20 in your case).
# stop: The ending value of the sequence (145 in your case).
# num: The number of values to generate (5 in your case).
# np.linspace(20, 145, 5) generates 5 equally spaced values between 20 and 145. The way these values are determined is based on dividing the interval [20, 145] into 4 equal parts, so the difference between consecutive values is consistent.

# Steps to calculate the values:
# The range from 20 to 145 is:
# 145
# −
# 20
# =
# 125
# 145−20=125
# To divide this range into 4 equal intervals, we divide the total range by 4 (since you want 5 points):

# 125/4 =31.25
# Starting from 20, we add 31.25 to each previous value to get the next one:
# First value: 20
# Second value: 
# 20+31.25 = 51.25
# 20+31.25=51.25
# Third value: 
# 51.25 + 31.25=82.5
# Fourth value: 
# 82.5 +31.25=113.75
# 113.75+31.25=145
print(data) # np.arange(20) creates an array of integers starting from 0 up to (but not including) 20. So, it generates the following array:2. np.sin(np.arange(20))
# np.sin() applies the sine function to each element of the array created by np.arange(20). The sine of each element is calculated based on its value in radians.  


# index of the maxima for each series

ind = data.argmax(axis=0)  #The function data.argmax(axis=0) finds the index of the maximum value along the specified axis. 
# In this case, axis=0 means you're finding the maximum value along each column of the data array.

# Let's take the data array you provided earlier:

# For each column, argmax gives the index of the maximum value:

# First column: The maximum value is 0.98935825 at index 2.
# Second column: The maximum value is 0.84147098 at index 0.
# Third column: The maximum value is 0.99060736 at index 3.
# Fourth column: The maximum value is 0.6569866 at index 1
print(ind)

#time corresponding to the maxima

time = np.array([ 20., 51.25, 82.5, 113.75, 145.])
ind = np.array([2, 0, 3, 1])  # result of data.argmax(axis=0)

time_max=time[ind]
data_max=data[ind,range(data.shape[1])]
print(time_max)
print(data_max)

if np.all(data_max == data.max(axis=0)):
    print(True)'''
 
# You can also use indexing with arrays as a target to assign to:

a = np.arange(5)
print(a)

a[[1,3,4]] = 0
print(a)

# However, when the list of indices contains repetitions, the assignment is done several times, leaving behind the last value:

a = np.arange(5)   #array([0, 1, 2, 3, 4])
a[[0,0,2]] = [1,2,3]   #a[0] = 1 (first assignment to index 0)
# a[0] = 2 (second assignment to index 0, overwriting the first one)
# a[2] = 3

print(a)

a = np.arange(5)
a[[0,0,2]] +=1

print(a)