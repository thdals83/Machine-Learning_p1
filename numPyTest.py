#!/usr/bin/env python
# -*- encoding: utf-8
# pip install numpy
import numpy as np

list1 = [1, 2, 3, 4]
a = np.array(list1)
print("a.shape : ", a.shape)  # (4, )
print()

b = np.array([[1, 2, 3], [4, 5, 6]])
print("b : ", b)
print()

print("b.shape : ", b.shape)  # (2, 3)
print()

print("b[0, 0] : ", b[0, 0])  # 1
print()

# all 0
a = np.zeros((2, 2))
print(a)
print()

# all 1
a = np.ones((2, 3))
print(a)
print()

# all 5
a = np.full((2, 3), 5)
print(a)
print()

# if row == column : 1
a = np.eye(3)
print(a)
print()

# sequence
a = np.array(range(20)).reshape((4, 5))
print(a)
