from gradient_search import gradient_min_search
from gradient_search import gradient_max_search
from aurea import aurea_min
from aurea import aurea_max
from math import cos

"""
    Nota:
    Controlo de erro é apenas mostrar o erro entre
"""

def f(x):
    return pow(2*x + 1, 2) - 5*cos(10*x)


tol = 0.001
x1 = -1
x2 = 0

print(f"aurea_min((2x + 1)^2 - 5cos(10x), {x1}, {x2}, {tol}) = {round(aurea_min(f, x1, x2, tol)[0], 4)}", sep="")
print(f"aurea_max((2x + 1)^2 - 5cos(10x), {x1}, {x2}, {tol}) = {round(aurea_max(f, x1, x2, tol)[0], 4)}", sep="")


def g(x, y):
    return y**2 - 2*x*y - 6*y + 2*(x**2) + 12


def dgx(x, y):
    return -2*y + 4*x


def dgy(x, y):
    return 2*y - 2*x - 6


x0 = 1
y0 = 1
h = 1

res = gradient_min_search(g, dgx, dgy, x0, y0, h, tol)
print(f"gradient_min_search(g, dgx, dgy, {x0}, {y0}, {h}, {tol}) =  ({round(res[0], 4)}, {round(res[1], 4)})", sep="")


def w(x, y):
    return 2*x*y + 2*x - x**2 - 2*(y**2)


def dwx(x, y):
    return 2*y + 2 - 2*x


def dwy(x, y):
    return 2*x - 4*y


x0 = -1
y0 = 1
h = 1

res = gradient_max_search(w, dwx, dwy, x0, y0, h, tol)
print(f"gradient_max_search(w, dwx, dwy, {x0}, {y0}, {h}, {tol}) =  ({round(res[0], 4)}, {round(res[1], 4)})", sep="")
