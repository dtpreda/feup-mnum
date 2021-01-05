import numpy as np
from matplotlib import pyplot as plt
from math import sin
from math import cos
from math import sqrt
from math import exp
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


h1 = 0.25
h2 = 0.125
h3 = 0.0625
a = 0
b = 2


def h(x, k=1.5):
    return sqrt(1 + (k*exp(k*x))**2)


def trap(f, a, b, h):
    fa, fb = f(a), f(b)
    res = fa + fb
    n  = round((b - a) / h)
    for i in range(1, n):
        a += h
        res += 2 * f(a)
    return (h/2) * res


def simp(f, a, b, h):
    fa, fb = f(a), f(b)
    res = fa + fb
    n = round((b - a) / h)
    for i in range(1, n):
        a += h
        if i % 2 == 0:
            res += 2 * f(a)
        else:
            res += 4 * f(a)
    return (h/3) * res


print(f"h: {h1}")
print(f"h': {h2}")
print(f"h'': {h3}")
print()

print(f"l trap: {trap(h, a, b, h1)} l simp: {simp(h, a, b, h1)}")
print(f"l' trap: {trap(h, a, b, h2)} l' simp: {simp(h, a, b, h2)}")
print(f"l'' trap: {trap(h, a, b, h3)} l'' simp: {simp(h, a, b, h3)}")
print()

print(f"QC trap: {(trap(h, a, b, h2) - trap(h, a, b, h1)) / (trap(h, a, b, h3) - trap(h, a, b, h2))}")
print(f"QC simp: {(simp(h, a, b, h2) - simp(h, a, b, h1)) / (simp(h, a, b, h3) - simp(h, a, b, h2))}")

print(f"Trap error: {(trap(h, a, b, h3) - trap(h, a, b, h2)) / 3}")
print(f"Trap error: {(simp(h, a, b, h3) - simp(h, a, b, h2)) / 15}")
print()

t0 = 2
T0 = 2
TA = 59


def dj(T, t=0):
    return -0.25 * (T - TA)


def euler(f, t0, T0, h, n):
    x, y, dx, dy = t0, T0, h, 0
    for i in range(n):
        dy = f(y, x)*dx
        y += dy
        x += dx
    return y


print(f"Integration result: {euler(dj, t0, T0, 0.5, 2)}")



