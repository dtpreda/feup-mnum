import numpy as np
from matplotlib import pyplot as plt
from math import sin
from math import cos
from zeroes import bissection_iter
from system import non_linear_newton_method_iter


def f(x):
    return sin(x) + x**5 - 0.2*x + 1


def dfx(x):
    return cos(x) + 5*(x**4) - 0.2


x = [x/10 for x in range(-12, 12)]
y = []
y2 = []
for i in x:
    y.append(f(i))
    y2.append(0)

"""
xarr = np.array(x)
yarr = np.array(y)
y2arr = np.array(y2)
plt.plot(xarr, yarr, "r")
plt.plot(xarr, y2arr, "b")
plt.show()
"""


res = bissection_iter(f, -1, 0, 6)
print(f"Root value: {res[0]}")
print(f"Absolute error: {res[1]}")
print(f"Relative error: {res[2]}")
print(f"Value at root: {f(res[0])}")
print()


def f1(x, y):
    return x**2 - y - 1.2


def f2(x, y):
    return -x + y**2 - 1


def f1dx(x, y):
    return 2*x


def f1dy(x, y):
    return -1


def f2dx(x, y):
    return -1


def f2dy(x, y):
    return 2*y


non_linear_newton_method_iter(f1, f2, f1dx, f1dy, f2dx, f2dy, 1, 1, 2)

