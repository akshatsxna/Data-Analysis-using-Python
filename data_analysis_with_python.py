# -*- coding: utf-8 -*-
"""Data Analysis with Python.ipynb


Basic Numpy Array
"""

import sys
import numpy as np

np.array([1, 2, 3, 4])

a = np.array([1, 2, 3, 4])

b = np.array([0, .5, 1, 1.5, 2])

a[0],a[1]

a[0:]

a[1:3]

a[1:-1]

a[::2]

b

b[0], b[2], b[-1]

b[[0,2,-1]]

"""Array Type"""

a

a.dtype

b

b.dtype

np.array([1, 2, 3, 4], dtype=np.float)

np.array([1, 2, 3, 4], dtype=np.int8)

c = np.array(['a', 'b', 'c'])

c.dtype

d = np.array([{'a': 1}, sys])

d.dtype

"""Dimensions & Shape"""

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

A.shape

A.ndim

A.size

B = np.array([
    [
        [12, 11, 10],
        [9, 8, 7],
    ],
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
])

B

B.shape

B.ndim

B.size

C = np.array([
    [
        [12, 11, 10],
        [9, 8, 7],
    ],
    [
        [6, 5, 4]
    ]
])

C

C.dtype

C.shape

C.size

type(C[0])

A = np.array([
#.   0. 1. 2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
])

A[1]

A[1][0]

A[1,0]

A[0:2]

A[:, :2]

A[:2, :2]

A[:2, 2:]

A

A[1] = np.array([10, 10, 10])

A

A[2]=99

A

"""Summary Statistics"""

a = np.array([1, 2, 3, 4])

a.sum()

a.mean()

a.var()

a.std()

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

A.sum()

A.mean()

A.std()

A.sum(axis=0)

A.sum(axis=1)

A.mean(axis=0)

A.mean(axis=1)

A.std(axis=0)

A.std(axis=1)

"""Broadcasting and Vectorized operations"""

a = np.arange(4)

a

a+10

a*10

a

a+=100

a

l=[0,1,2,3]

[i * 10 for i in l]

a = np.arange(4)

a

b = np.array([10, 10, 10, 10])

b

a+b

a*b

"""Boolean Array"""

a = np.arange(4)

a

a[0],a[-1]

a[[0, -1]]

a[[True, False, False, True]]

a

a >= 2

a[a >= 2]

a.mean()

a[a > a.mean()]

a[~(a > a.mean())]

a[(a == 0) | (a == 1)]

a[(a <= 2) & (a % 2 == 0)]

A = np.random.randint(100, size=(3, 3))

A

A[np.array([
    [True, False, True],
    [False, True, False],
    [True, False, True]
])]

A>30

A[A>30]

"""Linear Algebra"""

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])

A.dot(B)

A @ B

B.T

A

B.T@A

"""Size of Object in Memory

Int, Float
"""

# An integer in Python is > 24bytes
sys.getsizeof(1)

# Longs are even larger
sys.getsizeof(10**100)

# Numpy size is much smaller
np.dtype(int).itemsize

# Numpy size is much smaller
np.dtype(np.int8).itemsize

np.dtype(float).itemsize

"""Lists are even larger"""

# A one-element list
sys.getsizeof([1])

# An array of one element in numpy
np.array([1]).nbytes

"""performance is important"""

# Commented out IPython magic to ensure Python compatibility.
l = list(range(100000))
a = np.arange(100000)
# %time np.sum(a ** 2)

# Commented out IPython magic to ensure Python compatibility.
# %time sum([x ** 2 for x in l])

"""Useful NumPy function

Random
"""

np.random.random(size=2)
np.random.normal(size=2)
np.random.rand(2, 4)

"""Arange"""

np.arange(10)
np.arange(5, 10)
np.arange(0, 1, .1)

"""Reshape"""

np.arange(10).reshape(2, 5)
np.arange(10).reshape(5, 2)

"""Linspace"""

np.linspace(0, 1, 5)
np.linspace(0, 1, 20)
np.linspace(0, 1, 20, False)

""" zeros, ones, empty"""

np.zeros(5)
np.zeros((3, 3))
np.zeros((3, 3), dtype=np.int)
np.ones(5)
np.ones((3, 3))
np.empty(5)
np.empty((2, 2))

"""Identidy and eye """

np.identity(3)
np.eye(3, 3)
np.eye(8, 4)
np.eye(8, 4, k=1)
np.eye(8, 4, k=-3)
"Hello World"[6]

