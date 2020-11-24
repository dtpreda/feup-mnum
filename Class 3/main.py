from sympy import *
import math

x, y, z = symbols('x y z')
"""

def non_linear_system_picard_peano_error(g1, g2, x0, y0, e):
    
    Picard Peano method for solving non linear systems. Solution with e precision.
    Functions should be transformed from f1(x,y) = 0 (=) g1(x,y) = y and f2(x,y) = 0 (=) g2(x,y) = x.
    :param g1: function 1
    :param g2: function 2
    :param x0: approximate guess of x value of solution
    :param y0: approximate guess of y value of solution
    :param  e: precision error
    :return: tuple containing x and y values, respectively, of the solution
    
    if abs((diff(g1, x).subs(x, x0)).subs(y, y0)) + abs((diff(g2, x).subs(x, x0)).subs(y, y0)) >= 1 or abs(
            (diff(g1, y).subs(x, x0)).subs(y, y0)) + abs((diff(g2, y).subs(x, x0)).subs(y, y0)) >= 1:
        return None
    yn = (g1.subs(x, x0)).subs(y, y0)
    xn = (g2.subs(x, x0)).subs(y, y0)
    while not (abs(xn - x0) < e and abs(yn - y0) < e):
        print("g1(xn, yn): ", float(yn))
        print("g2(xn, yn): ", float(xn))
        print("--------------------------")
        y0 = yn
        x0 = xn
        yn = (g1.subs(x, x0)).subs(y, y0)
        xn = (g2.subs(x, x0)).subs(y, y0)
    return (xn, yn)


def get_f_at(f, xn, yn):
    return (f.subs(x, xn)).subs(y, yn)


def get_x_diff_at(f, xn, yn):
    return (diff(f, x).subs(x, xn)).subs(y, yn)


def get_y_diff_at(f, xn, yn):
    return (diff(f, y).subs(x, xn)).subs(y, yn)


def get_jacobian_at(j_matrix, x0, y0):
    return ((j_matrix.subs(x, x0)).subs(y, y0)).det()

# print("Picard Peano Result: ", non_linear_system_picard_peano_error(sqrt(x + 3*ln(x)), sqrt((5*x+x*y-1)/2), 4, 4, 0.00001))


def non_linear_system_newton_method_error(f1, f2, x0, y0, e):
    j = Matrix([f1, f2]).jacobian([x, y])
    xn = x0 - (get_f_at(f1, x0, y0)*get_y_diff_at(f2, x0, y0) - get_f_at(f2, x0, y0)*get_y_diff_at(f1, x0, y0))/get_jacobian_at(j, x0, y0)
    yn = y0 - (get_f_at(f2, x0, y0)*get_x_diff_at(f1, x0, y0) - get_f_at(f1, x0, y0) * get_x_diff_at(f2, x0, y0)) / get_jacobian_at(j, x0, y0)
    while abs(xn - x0) >= e or abs(yn - y0) >= e:
        print("xn: ", float(xn))
        print("yn: ", float(yn))
        print("--------------------------")
        x0 = xn
        y0 = yn
        xn = x0 - (get_f_at(f1, x0, y0) * get_y_diff_at(f2, x0, y0) - get_f_at(f2, x0, y0) * get_y_diff_at(f1, x0,y0)) / get_jacobian_at(j, x0, y0)
        yn = y0 - (get_f_at(f2, x0, y0) * get_x_diff_at(f1, x0, y0) - get_f_at(f1, x0, y0) * get_x_diff_at(f2, x0,y0)) / get_jacobian_at(j, x0, y0)
    return (float(xn), float(yn))


# print("Newton Method Result: ", non_linear_system_newton_method_error(2*x**2 + x*y - 5*x +1, x + 3*ln(x) - y**2, 4, 4, 0.000001))
"""


def f1(x0, y0):
    return 2*x0**2 - x0*y0 - 5*x0 + 1


def f1dx(x0, y0):
    return 4*x0 - y0 - 5


def f1dy(x0, y0):
    return -x0


def f2(x0, y0):
    return x0 + 3*math.log(x0) - y0**2


def f2dx(x0, y0):
    return 1 + 3/x0


def f2dy(x0, y0):
    return -2*y0


def non_linear_newton_method(f1, f2, f1dx, f1dy, f2dx, f2dy, x0, y0, e):
    xn = x0 - (f1(x0, y0) * f2dy(x0, y0) - f2(x0, y0) * f1dy(x0, y0)) / (
                f1dx(x0, y0) * f2dy(x0, y0) - f2dx(x0, y0) * f1dy(x0, y0))
    yn = y0 - (f2(x0, y0) * f1dx(x0, y0) - f1(x0, y0) * f2dx(x0, y0)) / (
                f1dx(x0, y0) * f2dy(x0, y0) - f2dx(x0, y0) * f1dy(x0, y0))
    while abs(xn - x0) >= e or abs(yn - y0) >= e:
        print("xn: ", float(xn))
        print("yn: ", float(yn))
        print("--------------------------")
        x0 = xn
        y0 = yn
        xn = x0 - (f1(x0, y0) * f2dy(x0, y0) - f2(x0, y0) * f1dy(x0, y0)) / (
                    f1dx(x0, y0) * f2dy(x0, y0) - f2dx(x0, y0) * f1dy(x0, y0))
        yn = y0 - (f2(x0, y0) * f1dx(x0, y0) - f1(x0, y0) * f2dx(x0, y0)) / (
                    f1dx(x0, y0) * f2dy(x0, y0) - f2dx(x0, y0) * f1dy(x0, y0))
    return (float(xn), float(yn))


print("Newthon's Method Result: ", non_linear_newton_method(f1, f2, f1dx, f1dy, f2dx, f2dy, 4, 4, 0.000001))


def get_jacobian_at(f1dx, f2dx, f1dy, f2dy, x0, y0):
    return ((f1dx.subs(x, x0)).subs(y, y0) * (f2dy.subs(x, x0)).subs(y, y0) - (f2dx.subs(x, x0)).subs(y, y0) * (f1dy.subs(x, x0)).subs(y, y0))


def sympy_non_linear_newton_method(f1, f2, x0, y0, e): # too slow for such a simple algorithm
    f1dx = diff(f1, x)
    f2dx = diff(f2, x)
    f1dy = diff(f1, y)
    f2dy = diff(f2, y)
    xn = x0 - ((f1.subs(x, x0)).subs(y, y0)*(f2dy.subs(x,x0)).subs(y, y0) - (f2.subs(x, x0)).subs(y, y0)*(f1dy.subs(x,x0)).subs(y, y0))/get_jacobian_at(f1dx, f2dx, f1dy, f2dy, x0, y0)
    yn = y0 - ((f2.subs(x, x0)).subs(y, y0)*(f1dx.subs(x,x0)).subs(y, y0) - (f1.subs(x, x0)).subs(y, y0)*(f2dx.subs(x,x0)).subs(y, y0))/get_jacobian_at(f1dx, f2dx, f1dy, f2dy, x0, y0)
    while abs(xn - x0) >= e or abs(yn - y0) >= e:
        print("xn: ", float(xn))
        print("yn: ", float(yn))
        print("--------------------------")
        x0 = xn
        y0 = yn
        xn = x0 - ((f1.subs(x, x0)).subs(y, y0) * (f2dy.subs(x, x0)).subs(y, y0) - (f2.subs(x, x0)).subs(y, y0) * (
            f1dy.subs(x, x0)).subs(y, y0)) / get_jacobian_at(f1dx, f2dx, f1dy, f2dy, x0, y0)
        yn = y0 - ((f2.subs(x, x0)).subs(y, y0) * (f1dx.subs(x, x0)).subs(y, y0) - (f1.subs(x, x0)).subs(y, y0) * (
            f2dx.subs(x, x0)).subs(y, y0)) / get_jacobian_at(f1dx, f2dx, f1dy, f2dy, x0, y0)
    return (float(xn), float(yn))


# print("Newthon's Method Result: ", sympy_non_linear_newton_method(2*x**2 - x*y - 5*x +1, x + 3*ln(x) - y**2, 4, 4, 0.000001))