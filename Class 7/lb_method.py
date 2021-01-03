from quadratic import build_inv_hessian
from quadratic import matrix_mul


def lb_method(f, dfx, dfy, dfxx, dfxy, dfyx, dfyy, x0, y0, lmbd, e=1e-4):
    while True:
        hess = build_inv_hessian(x0, y0, dfxx, dfxy, dfyx, dfyy)
        grad = [dfx(x0, y0), dfy(x0, y0)]
        hess_grad = matrix_mul(hess, grad)
        x = x0 - lmbd * dfx(x0, y0) - hess_grad[0]
        y = y0 - lmbd * dfy(x0, y0) - hess_grad[1]
        print(x, y, lmbd)
        if f(x, y) < f(x0, y0):
            if abs(x - x0) < e and abs(y - y0) < e:
                return x, y
            lmbd *= 0.5
            x0 = x
            y0 = y
        else:
            lmbd *= 2

