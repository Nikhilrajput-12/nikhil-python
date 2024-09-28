import numpy as np

#1.using list or tuple
'''a =np.array([2,3])
print(a)

a =np.array((2,3))
print(a)
'''

# 2.Predefined Array Creation

'''b=np.zeros((2, 3))  # 2x3 array of zeros    np.zeros(shape)
a=np.ones((2, 3))  # 2x3 array of ones      np.ones(shape)
print(a)
print(b)


c=np.full((2, 3), 7)     # 2x3 array filled with 7s     np.full(shape, value)

d=np.empty((2, 3))  # 2x3 array with random data
print(d)

'''


# 3. Sequences and Ranges
'''a=np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]     np.arange(start, stop, step)
print(a)  

b=np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]   np.linspace(start, stop, num)
print(b)

c=np.logspace(1, 3, 3)  # [10.0, 100.0, 1000.0]  np.logspace(start, stop, num, base=10.0)
print(c)            #: Generates numbers spaced evenly on a logarithmic scale.
'''


# 5. Random Arrays
# np.random.rand(d0, d1, ..., dn): #Creates an array of the given shape with random values between 0 and 1 (uniform distribution).

a=np.random.rand(2, 3)  # 2x3 array of random floats
print(a)


# np.random.randint(low, high, size): Creates an array of random integers between low and high.

b=np.random.randint(0, 10, (2, 3))  # 2x3 array of random integers between 0 and 9
print(b)


# np.random.randn(d0, d1, ..., dn): Creates an array of the given shape with random values drawn from a standard normal distribution.


c=np.random.randn(2, 3)  # 2x3 array of random floats from normal distribution
print(c)


# np.random.default_rng(): Use the new random number generator.

rng = np.random.default_rng(42)
d=rng.random((2, 3))  # Random 2x3 array
print(d)