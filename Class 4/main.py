from copy import deepcopy


def gauss_elimination(matrix, solutions):
    """
        Gauss Elimination Method. Puts the Matrix in an inferior triangle shape through Jacobi Operations.
    """
    for i in range(0, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            const = -matrix[j][i] / matrix[i][i]
            # print("const = matrix[", j + 1, "][", i + 1, "]/matrix[", i + 1, "][", i + 1, "]: ", const)
            for k in range(0, len(matrix[j])):
                matrix[j][k] += const * matrix[i][k]
            solutions[j] += const * solutions[i]
        # print(matrix, "\n---------------")  # uncomment to see matrix being solved
    return matrix


def gauss_elimination_solve(matrix, solutions):
    """
        Gauss Elimination Method. Matrix should be in inferior triangle shape (see gauss_elimination).
        Solves the system by solving each equation of the final system given by the multiplication of the two matrices.
        Returns solution of the system.
    """
    res = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = round(matrix[i][j], 3)
    if matrix[len(matrix) - 1][len(matrix) - 1] == 0:
        res.append(0)
    else:
        res.append(solutions[len(solutions) - 1] / matrix[len(matrix) - 1][len(matrix) - 1])
    for i in range(1, len(solutions)):
        var = solutions[len(solutions) - i - 1]
        for k in range(0, len(matrix[0])):
            if len(matrix) - k - 1 == len(matrix) - i - 1:
                continue
            elif k < len(res):
                var -= matrix[len(matrix) - i - 1][len(matrix) - k - 1] * res[k]
        if matrix[len(matrix) - i - 1][len(matrix) - i - 1] == 0:
            res.append(0)
        else:
            res.append(var / matrix[len(matrix) - i - 1][len(matrix) - i - 1])
    res.reverse()
    for i in range(0, len(res)):
        res[i] = round(res[i], 3)
    return res


def gauss_elimination_inverted_solve(matrix, solutions):
    """
        Gauss Elimination Method for a superior triangle shaped matrix.
        Solves the system by solving each equation of the final system given by the multiplication of the two matrices.
        Returns solution of the system.
    """
    res = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = round(matrix[i][j], 3)
    if matrix[0][0] == 0:
        res.append(0)
    else:
        res.append(solutions[0] / matrix[0][0])
    for i in range(1, len(matrix[0])):
        var = solutions[i]
        for j in range(0, i):
            if i == j:
                continue
            var -= matrix[i][j] * res[j]
        if matrix[i][i] == 0:
            res.append(0)
        else:
            res.append(var / matrix[i][i])
    for k in range(0, len(res)):
        res[k] = round(res[k], 3)
    return res


def gauss_elimination_internal_stability(matrix, solutions):
    """
        Calculates internal stability of a solution given by the Gauss Elimination Method.
    """
    stab = []
    backup_matrix = deepcopy(matrix)
    backup_solutions = deepcopy(solutions)
    res = gauss_elimination_solve(matrix, solutions)
    for i in range(0, len(backup_matrix)):
        temp = 0
        for j in range(0, len(backup_matrix[i])):
            temp += backup_matrix[i][j] * res[j]
        temp -= backup_solutions[i]
        stab.append(round(temp, 3))
    return stab


def gauss_elimination_external_stability(matrix, solutions, delta_a, delta_b):
    """
            Calculates external stability of a solution given by the Gauss Elimination Method.
    """
    backup_matrix = deepcopy(matrix)
    res = gauss_elimination_solve(matrix, solutions)
    new_res = []
    for i in range(0, len(res)):
        temp = 0
        for j in range(0, len(res)):
            temp += res[j] * delta_a
        temp = delta_b - temp
        new_res.append(temp)
    return gauss_elimination_solve(backup_matrix, new_res)


m = [[1, 4, 9, 16], [4, 9, 16, 25], [9, 16, 25, 36], [16, 25, 36, 49]]
sol = [30, 54, 86, 126]

# print(gauss_elimination_solve(m, sol))

m = [[7, 2, 6], [4, 10, 1], [5, -2, 8]]
sol = [24, 27, 27]


# print(gauss_elimination_solve(m, sol))
# print(gauss_elimination_internal_stability(m, sol))
# print(gauss_elimination_external_stability(m, sol, 0.5, 0.2))


def khalesky_build_matrices(matrix):
    """
        Calculates matrices needed for Khalesky's method for solving linear systems.
        Returns a list with L and U matrices.
    """
    l, u, temp = [], [], []
    for i in range(0, len(matrix[0])):
        l.append([matrix[i][0]])
    for j in range(0, len(matrix)):
        temp.append(matrix[0][j] / l[0][0])
    u.append(temp)
    for k in range(1, len(matrix)):
        for n in range(0, len(matrix)):
            tmp = 0
            for o in range(0, k):
                tmp += l[n][o] * u[o][k]
            l[n].append(matrix[n][k] - tmp)
        temp = []
        for p in range(0, len(matrix)):
            tmp = 0
            for q in range(0, k):
                tmp += l[k][q] * u[q][p]
            temp.append((matrix[k][p] - tmp) / l[k][k])
        u.append(temp)
    return [l, u]


def khalesky_solve(matrix, solutions):
    """
        Khalesky Method for solving linear systems.
    """
    matrices = khalesky_build_matrices(matrix)
    l, u = matrices[0], matrices[1]
    y = gauss_elimination_inverted_solve(l, solutions)
    res = gauss_elimination_solve(u, y)
    for i in range(0, len(res)):
        res[i] = round(res[i], 3)
    return res


# print(khalesky_solve(m, sol))


def gauss_conv_condition(matrix):
    for i in range(0, len(matrix)):
        var, temp = 0, 0
        for j in range(0, len(matrix[i])):
            if i == j:
                var = matrix[i][j]
            else:
                temp += matrix[i][j]
        if var <= temp:
            return False
    return True


def gauss_jacobi_solve(matrix, solutions, guesses):
    if not (gauss_conv_condition(matrix)):
        return None
    last = []
    check = False
    while True:
        # print("last: ", last)
        # print("guesses: ", guesses)
        for i in range(0, len(last)):
            if abs(guesses[i] - last[i]) >= 0.00001:
                check = False
                break
            check = True
        if check:
            for k in range(0, len(guesses)):
                guesses[k] = round(guesses[k], 3)
            return guesses
        last = [x for x in guesses]
        for i in range(0, len(guesses)):
            temp = solutions[i]
            for j in range(0, len(matrix)):
                if i == j:
                    continue
                temp -= matrix[i][j] * last[j]
            guesses[i] = temp / matrix[i][i]


m = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
sol = [7, 4, 5]
init = [0, 0, 0]

# print(gauss_jacobi_solve(m, sol, init), "\n--------------------------------------")


def gauss_seidel_solve(matrix, solutions, guesses):
    if not (gauss_conv_condition(matrix)):
        return None
    last = []
    check = False
    while True:
        # print("last: ", last)
        # print("guesses: ", guesses)
        for i in range(0, len(last)):
            if abs(guesses[i] - last[i]) >= 0.00001:
                check = False
                break
            check = True
        if check:
            for k in range(0, len(guesses)):
                guesses[k] = round(guesses[k], 3)
            return guesses
        last = [x for x in guesses]
        for i in range(0, len(guesses)):
            temp = solutions[i]
            for j in range(len(matrix) - 1, i - 1, -1):
                if i == j:
                    continue
                temp -= matrix[i][j] * last[j]
            for k in range(0, i):
                temp -= matrix[i][k] * guesses[k]
            guesses[i] = temp / matrix[i][i]


m = [[3, 1, 1], [1, 4, 2], [0, 2, 5]]
sol = [7, 4, 5]
init = [0, 0, 0]

# print(gauss_seidel_solve(m, sol, init))