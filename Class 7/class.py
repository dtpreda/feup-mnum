def f(x, y):
    return (x-40)**2 + y**2


def fx(x, y):
    return 2*(x-40)


def fy(x, y):
    return 2*y


# h, x0, e y0 são arbitrarios
def gradient_search(f, fx, fy, x0, y0, h, e=1e-4):
    x = x0
    y = y0
    while True:
        xnext = x - h*fx(x, y)
        ynext = y - h*fy(x ,y)
        if f(x,y) < f(xnext, ynext):
            h /= 2
        else:
            if abs(xnext - x) + abs(ynext - y) < e:
                return round(xnext, 4), round(ynext, 4)
            h *= 2
            x, y = xnext, ynext
            print(x, y, h)


def coordinated(f, fx, fy, x0, y0, h, e=1e-4):
    x, y = x0, y0
    while True:
        xnext = x - h*fx(x,y)
        if f(x, y) < f(xnext, y):
            h /= 2
        else:
            if abs(xnext - x) < e:
                x = xnext
                break;
            h *= 2
            x = xnext
            print(x, h)
    print("----------")
    while True:
        ynext = y - h*fy(x,y)
        if f(x, y) < f(x, ynext):
            h /= 2
        else:
            if abs(ynext - y) < e:
                return round(x, 4), round(ynext, 4)
            h *= 2
            y = ynext
            print(y, h)


x0, y0 = 3, 4
h = 15
# print(f"gradient search({f}, {fx}, {fy}, {x0}, {y0}, {h}) = ", gradient_search(f, fx, fy, x0, y0, h), sep="");

print(f"coordinated(f, fx, fy, {x0}, {y0}, {h}) = ", coordinated(f, fx, fy, x0, y0, h), sep="")