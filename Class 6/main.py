"""
    Quociente de Convergência:
    S(n) -> solução do ponto n com step = h
    S'(2n) -> solução do ponto 2n com step = h/2
    S''(4n) -> solução do ponto 4n com step = h/4
    QC = 2**ordem
    E''(n) = (S''-S')/(2**n - 1)
"""

xi = 0
xfinal = 5
yi = 1
n1 = 10000
n2 = n1*2
n4 = n2*2


def f1(x,y):
    return x**2


def f2(x,y):
    return x**3/3 + 1


def euler_method(f, x0, y0, xf, n): # o erro reduz para metade com o dobro das operações => ordem 2
    x, y, dx, dy = x0, y0, (xf - x0)/n, 0
    for i in range(0, n):
        dy = f(x, y) * dx
        y += dy
        x += dx
        # print("(x: ", x, ",y: ", y, ")\nError: ", abs(y - f2(x,y)), "\n")
    return x, y


print("\nEuler Method Result: ", euler_method(f1, xi, yi, xfinal, n4), sep="")

qc = (euler_method(f1, xi, yi, xfinal, n2)[1] - euler_method(f1, xi, yi, xfinal, n1)[1])/(euler_method(f1, xi, yi, xfinal, n4)[1] - euler_method(f1, xi, yi, xfinal, n2)[1])

print("Quociente de Convergência (Euler): ", qc, sep="") # Suposto tender para 2
print("Epsilon\" (Euler): ", abs(euler_method(f1, xi, yi, xfinal, n4)[1] - euler_method(f1, xi, yi, xfinal, n2)[1]), sep="") # Suposto tender para 0


def rk2(f, x0, y0, xf, n):
    x, y, dx, dy = x0, y0, (xf - x0) / n, 0
    for i in range(0, n):
        dy = f(x + dx*0.5, y + dx*f(x, y))*dx
        y += dy
        x += dx
        # print("(x: ", x, ",y: ", y, ")\nError: ", abs(y - f2(x,y)), "\n")
    return x, y


print("\nRK2 Result: ", rk2(f1, xi, yi, xfinal, n4), sep="")

qc = (rk2(f1, xi, yi, xfinal, n2)[1] - rk2(f1, xi, yi, xfinal, n1)[1]) / (rk2(f1, xi, yi, xfinal, n4)[1] - rk2(f1, xi, yi, xfinal, n2)[1])

print("Quociente de Convergência (RK2): ", qc, sep="") # QC IS COMING OUT WRONG, SHOULD => 4
print("Epsilon\" (RK2): ", abs(rk2(f1, xi, yi, xfinal, n4)[1] - rk2(f1, xi, yi, xfinal, n2)[1]), sep="")

print("\nReal Result: (", 5, ", ", f2(5, 0), ")", sep="")
