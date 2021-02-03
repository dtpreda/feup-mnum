import math


def f1(x, y):
    return math.sin(x + y) - math.exp(x - y)


def f2(x, y):
    return math.cos(x + y) - (x**2)*(y**2)


def df1x(x, y):
    return math.cos(x + y) - math.exp(x - y)


def df1y(x, y):
    return math.cos(x + y) - math.exp(x - y)


def df2x(x, y):
    return -math.sin(x + y) - 2*x*(y**2)


def df2y(x, y):
    return -math.sin(x + y) - 2*y*(x**2)


def newton (x, y, f1, f2, f1dx, f1dy, f2dx, f2dy, n):
    for i in range(n):
        print(x, y)
        x = x - (f1(x, y)*f2dy(x, y) - f2(x, y)*f1dy(x, y))/(f1dx(x, y)*f2dy(x, y) - f1dy(x, y)*f2dx(x, y))
        y = y - (f2(x, y)*f1dy(x, y) - f1(x, y)*f2dy(x, y))/(f1dx(x, y)*f2dy(x, y) - f1dy(x, y)*f2dx(x, y))
    print(x, y)


def dy(x, y, z):
    return z


def dz(x, y, z):
    return -7*z - 4*y


def euler(x, y, z, h, f1, f2, n):
    dx, dy, dz = h, 0, 0
    for i in range(n):
        dy = f1(x, y, z)*dx
        dz = f2(x, y, z)*dx
        y += dy
        z += dz
        x += dx
        print(f"x: {x} y: {y} z: {z}")


if __name__ == "__main__":
    print("Método de Newton:")
    newton(0.5, 0.25, f1, f2, df1x, df1y, df2x, df2y, 2)
    print()
    print(f"Regra de Simpson (Cubatura): {1/9 * (1.1 + 9.8 + 1.2 + 7.8 + 4*(1.5 + 1.4 + 2.1 + 2.2) + 16*4)}")
    print()
    print("Método de Euler:")
    euler(0.4, 2, 1, 0.2, dy, dz, 3)