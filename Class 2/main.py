from sympy import *

x, y, z = symbols('x y z')


def bissection_abs(f, a, b):
    """
        Bissection Method, stopping with the most precision the computer can handle.
        Finds a real root of f, comprised between a and b.
    """
    if f.subs(x, a) * f.subs(x, b) > 0:  # this means there isn't any evidence of a real root between a and b, therefore
        # the result may be invalid
        return None
    m = (a + b) / 2
    while m != a and m != b:
        # print("a: ", a)
        # print("b: ", b)
        # print("m: ", m)
        # print("----------------------------------------")
        if f.subs(x, a) * f.subs(x, m) <= 0:
            b = m
        else:
            a = m
        m = (a + b) / 2
    return float(m)


# print("Bissection Method result:", bissection_abs(x**3-27, -1, 5))

def regula_falsi_abs(f, a, b):
    """
        Regula Falsi Method, stopping with the most precision the computer can handle.
        Finds a real root of f, comprised between a and b.
    """
    if f.subs(x, a) * f.subs(x, b) > 0:
        return None
    xn = (f.subs(x, b) * a - f.subs(x, a) * b) / (f.subs(x, b) - f.subs(x, a))
    while xn != a and xn != b:
        # print("a: ", a)
        # print("b: ", b)
        # print("xn: ", xn)
        # print("----------------------------------------")
        if f.subs(x, a) * f.subs(x, xn) <= 0:
            b = xn
        else:
            a = xn
        xn = (f.subs(x, b) * a - f.subs(x, a) * b) / (f.subs(x, b) - f.subs(x, a))
    return float(xn)


# print("Regula Falsi result:", regula_falsi_abs(x**3-27, -2.9, 3.1))

def newton_error(f, x0, e):
    """
            Newton Method, stopping with precision equal to e.
            Finds a real root of f, in the surroundings of the guess value x0.
        """
    xn0 = x0
    xn = x0 - (f.subs(x, x0) / diff(f, x).subs(x, x0))
    while abs(xn - xn0) >= e:
        # print("xn-1: ", float(xn0))
        # print("xn: ", float(xn))
        # print("----------------------------------------")
        xn0 = xn
        xn = xn0 - (f.subs(x, xn0) / diff(f, x).subs(x, xn0))
    return float(xn)


# print("Newton method result:", newton_error(x**3 - 27, 1, 0.0000000000001))

def picard_peano_error(g, x0, e):
    if abs(diff(g, x).subs(x, x0)) >= 1:  # necessary condition for Picard Peano method
        return "Impossible to solve with Picard Peano Method"
    xn = g.subs(x, x0)
    while abs(xn - x0) >= e:
        # print("x0: ", float(x0))
        # print("xn: ", float(xn))
        # print("----------------------------------------")
        x0 = xn
        xn = g.subs(x, x0)
        if abs(diff(g, x).subs(x, x0)) >= 1:  # necessary condition for Picard Peano method
            return "Impossible to solve with Picard Peano Method"
    return float(xn)


# print("Picard Peano result:", picard_peano_error(sqrt(x/4), 4, 0.0000000000001))
# solves sqrt(x)/2 - 1 = 0 with g(x) = sqrt(x/4)

