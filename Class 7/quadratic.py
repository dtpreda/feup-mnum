def build_inv_hessian(x, y, dfxx, dfxy, dfyx, dfyy):
    f, s = [], []
    if dfxx(x, y) == 0:
        f.append(0)
    else:
        f.append(1/dfxx(x, y))
    if dfyx(x, y) == 0:
        f.append(0)
    else:
        f.append(1 / dfyx(x, y))
    if dfxy(x, y) == 0:
        s.append(0)
    else:
        s.append(1 / dfxy(x, y))
    if dfyy(x, y) == 0:
        s.append(0)
    else:
        s.append(1 / dfyy(x, y))
    return f, s


def matrix_mul(m1, m2):
    if len(m1[0]) != len(m2):
        return None
    l1, l2, res = 0, 0, []
    for i in range(len(m1)):
        l1 += m1[0][i] * m2[i]
        l2 += m1[1][i] * m2[1]
    res = [l1, l2]
    return res


def quadratic_min(f, dfx, dfy, dfxx, dfxy, dfyx, dfyy, x0, y0, e=1e-4):
    while True:
        hess = build_inv_hessian(x0, y0, dfxx, dfxy, dfyx, dfyy)
        grad = [dfx(x0, y0), dfy(x0, y0)]
        hess_grad = matrix_mul(hess, grad)
        x = x0 - hess_grad[0]
        y = y0 - hess_grad[1]
        # print(x, y)
        if abs(x - x0) < e and abs(y - y0) < e:
            return x, y
        x0 = x
        y0 = y
