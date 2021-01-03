def bissection_iter(f, a, b, n):
    """
        Bissection Method, stopping with the most precision the computer can handle.
        Finds a real root of f, comprised between a and b.
    """
    if f(a) * f(b) > 0:  # this means there isn't any evidence of a real root between a and b, therefore
        # the result may be invalid
        return None
    error, rel_error = 0, 0
    for i in range(n):
        m = (a + b) / 2
        # print("a: ", a)
        # print("b: ", b)
        # print("m: ", m)
        # print("----------------------------------------")
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
        error = abs(((a + b) / 2) - m)
        rel_error = error/((a + b) / 2)
    return float(m), error, rel_error
