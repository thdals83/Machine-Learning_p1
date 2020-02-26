#!/usr/bin/env python
# -*- encoding: utf-8

import time
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

A = np.random.random(size=(10000, 10000))

cpuTime = time.process_time()    # CPU time
wallTime1 = time.perf_counter()   # wall time
wallTime2 = time.time()            # wall time

cpuTime = time.process_time()-cpuTime     # CPU time
wallTime1 = time.perf_counter()-wallTime1   # wall time
wallTime2 = time.time()-wallTime2           # wall time

print('cpuTime : ', cpuTime)
print('wallTime1 : ', wallTime1)
print('wallTime2 : ', wallTime2)

image = misc.face(gray=True).astype(np.float32)
derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
ck = signal.cspline2d(image, 8.0)
deriv = (signal.sepfir2d(ck, derfilt, [1]) +
         signal.sepfir2d(ck, [1], derfilt))

laplacian = np.array([[0,1,0], [1,-4,1], [0,1,0]], dtype=np.float32)
deriv2 = signal.convolve2d(ck,laplacian,mode='same',boundary='symm')

plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()
