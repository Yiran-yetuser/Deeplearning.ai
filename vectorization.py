import numpy as np
import time

a = np.random.rand(100000000)
b = np.random.rand(100000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()
time1 = float(1000 * (toc - tic))
print("Vectorized version:" + str(time1) + "ms")
print(c)

c = 0
tic = time.time()
for i in range(100000000):
    c += a[i] * b[i]
toc = time.time()
time2 = 1000 * (toc - tic)
print("For loop:" + str(time2) + "ms")
print(c)

print("Multiple by " + str(time2 / time1))
