import math

B = (math.sqrt(5) - 1)/2
A = pow(B, 2)


def aurea_min(f, x1, x2, e=1e-4):
    while abs(x2 - x1) >= e:
        x3 = x1 + A*(x2 - x1)
        x4 = x1 + B*(x2 - x1)
        if f(x3) < f(x4):
            x2 = x4
        elif f(x3) > f(x4):
            x1 = x3
    return x1, x2


def aurea_max(f, x1, x2, e=1e-4):
    while abs(x2 - x1) >= e:
        x3 = x1 + A*(x2 - x1)
        x4 = x1 + B*(x2 - x1)
        if -f(x3) < -f(x4):
            x2 = x4
        elif -f(x3) > -f(x4):
            x1 = x3
    return x1, x2
