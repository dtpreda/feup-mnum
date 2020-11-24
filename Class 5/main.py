from math import pi
from math import sin


def trapezoidal_rule(f, a, b, h):
    res = f(a) + f(b)
    for i in range(1, round((b-a)/h) + 1):
        res += 2*f(a + i*h)
    return (h/2)*res


# print(trapezoidal_rule(sin, 0, pi, pi/64))


def simpson_rule(f, a, b, h):
    res = f(a) + f(b)
    for i in range(1, round((b-a)/h), 2):
        res += 4*f(a + i*h)
    for j in range(2, round((b-a)/h), 2):
        res += 2*f(a + j*h)
    return h/3*res


# print(simpson_rule(sin, 0, pi, pi/64))