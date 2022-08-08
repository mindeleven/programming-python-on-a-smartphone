import numpy as np

# from the numpy documentation:
# numpy's main object id a multdimensional array
# a table of elements, all of the same type
# usually numbers
# indexed by a tuple of non-negative integers
# dimensions are called axes
# example: one axis with three elements
# [1, 2, 1]
# two axis with three elements each
# [[1, 4, 6], [3, 7, 8]]

# numpy's array class id called nd array
a = np.arange(15).reshape(3, 5)

print(a)