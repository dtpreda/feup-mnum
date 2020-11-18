def gauss_elimination(matrix):
    """
        Gauss Elimination Method. Puts the Matrix in an inferior triangle shape through Jacobi Operations.
    """
    for i in range(0, len(matrix) - 1):
        # print(matrix, "\n---------------") # uncomment to see matrix being solved
        for j in range(i + 1, len(matrix)):
            const = -matrix[j][i]/matrix[i][i]
            for k in range(0, len(matrix[j])):
                matrix[j][k] += const*matrix[i][k]
    return matrix


def gauss_elimination_solve(matrix, solutions):
    """
        Gauss Elimination Method. Puts the Matrix in an inferior triangle shape through Jacobi Operations.
        Solves the system by solving each equation of the final system given by the multiplication of the two matrices.
        Returns solution of the system.
    """
    res = []
    for i in range(0, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            const = -matrix[j][i]/matrix[i][i]
            # print("const = matrix[", j + 1, "][", i + 1, "]/matrix[", i + 1, "][", i + 1, "]: ", const)
            for k in range(0, len(matrix[j])):
                matrix[j][k] += const*matrix[i][k]
            solutions[j] += const*solutions[i]
        print(matrix, "\n---------------")  # uncomment to see matrix being solved
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = round(matrix[i][j], 3)
    if matrix[len(matrix) - 1][len(matrix) - 1] == 0:
        res.append(0)
    else:
        res.append(solutions[len(solutions) - 1]/matrix[len(matrix) - 1][len(matrix) - 1])
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
            res.append(var/matrix[len(matrix) - i - 1][len(matrix) - i - 1])
    res.reverse()
    for i in range(0, len(res)):
        res[i] = round(res[i], 3)
    return res


m = [[1, 4, 9, 16], [4, 9, 16, 25], [9, 16, 25, 36], [16, 25, 36, 49]]
sol = [30, 54, 86, 126]

# print(gauss_elimination_solve(m, sol))

m = [[7,2,6],[4,10,1],[5,-2,8]]
sol = [24,27,27]
print(gauss_elimination_solve(m, sol))