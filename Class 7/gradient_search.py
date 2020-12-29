def gradient_min_search(f, dfx, dfy, x0, y0, h, e=1e-4):
    iterations = 0
    xerror = 0
    while True:
        iterations += 1
        x = x0 - h * dfx(x0, y0)
        y = y0 - h * dfy(x0, y0)
        if f(x, y) < f(x0, y0):
            h *= 2
            # print(x, y, h, sep = ", ")
            if abs(x - x0) < e and abs(y - y0):
                # print(f"iterations: {iterations}", sep="")
                return x, y
            x0 = x
            y0 = y
        else:
            h /= 2


def gradient_max_search(f, dfx, dfy, x0, y0, h, e=1e-4):
    iterations = 0
    while True:
        iterations += 1
        # print(f"f({x0}, {y0}): {f(x0, y0)}, h: {h}")
        x = x0 + h * dfx(x0, y0)
        y = y0 + h * dfy(x0, y0)
        if -f(x, y) < -f(x0, y0):
            h *= 2
            # print(x, y, h, sep = ", ")
            if abs(x - x0) < e and abs(y - y0) < e:
                # print(f"iterations: {iterations}", sep="")
                return x, y
            x0 = x
            y0 = y
        else:
            h /= 2
