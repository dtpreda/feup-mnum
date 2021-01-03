def non_linear_newton_method_iter(f1, f2, f1dx, f1dy, f2dx, f2dy, x0, y0, n):
    for i in range(n):
        xn = x0 - (f1(x0, y0) * f2dy(x0, y0) - f2(x0, y0) * f1dy(x0, y0)) / (
                f1dx(x0, y0) * f2dy(x0, y0) - f2dx(x0, y0) * f1dy(x0, y0))
        yn = y0 - (f2(x0, y0) * f1dx(x0, y0) - f1(x0, y0) * f2dx(x0, y0)) / (
                f1dx(x0, y0) * f2dy(x0, y0) - f2dx(x0, y0) * f1dy(x0, y0))
        x0 = xn
        y0 = yn
        print("xn: ", float(xn))
        print("yn: ", float(yn))
        print("--------------------------")
    return float(xn), float(yn)
