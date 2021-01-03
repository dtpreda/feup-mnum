from gradient_search import gradient_min_search
from gradient_search import gradient_max_search
from aurea import aurea_min
from aurea import aurea_max
from quadratic import quadratic_min
from lb_method import lb_method
from math import cos
from math import sin

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
print()


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
print()


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


def j(x, y):
    return sin(x/2) + x**2 - cos(y)


def djx(x, y=0):
    return 0.5*cos(x/2) + 2*x


def djy(x, y):
    return sin(y)


def djxx(x, y):
    return -0.25*sin(x/2) + 2


def djxy(x, y):
    return 0


def djyx(x, y):
    return 0


def djyy(x, y):
    return cos(y)


x0 = -3
y0 = -1

res = quadratic_min(j, djx, djy, djxx, djxy, djyx, djyy, x0, y0, tol)
print(f"quadratic_min(j, djx, djy, djxx, djxy, djyx, djyy, {x0}, {y0}, {tol}) = ({round(res[0], 6)}, {round(res[1], 6)})", sep="")
print()


x0 = -10
y0 = -1
lmbd = 0.01

res = lb_method(j, djx, djy, djxx, djxy, djyx, djyy, x0, y0, lmbd, tol)
print(f"lb_method(j, djx, djy, djxx, djxy, djyx, djyy, {x0}, {y0}, {lmbd}, {tol}) = ({round(res[0], 6)}, {round(res[1], 6)})", sep="")
print()
