import numpy as np


def derterminant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    all_matrix = []

    for i in range(len(matrix)):
        new_matrix = []
        for j in range(1, len(matrix)):
            new_matrix.append([])
            for k in range(0, len(matrix)):
                if (i + k + 1) % len(matrix) == i:
                    print("werwt")
                    pass
                # print(j)
                else:
                    new_matrix[j-1].append(matrix[j][(i + k + 1) % len(matrix)])

        all_matrix.append(new_matrix)

    sum = 0

    for i in range(len(all_matrix)):
        print(all_matrix[i])
        print(matrix[0][i])
        print(derterminant(all_matrix[i]))
        print(np.linalg.det(all_matrix[i]), ' hhh')
        sum += matrix[0][i] * derterminant(all_matrix[i]) * ((-1)**i)
        print(sum)

    return sum



def inverse(Matrix):
    pass

matrix_1 = [[1, 2], [1, 2]]
matrix = [[1, 2, 3], [0, 4, 5], [1, 0, 6]]
print(derterminant(matrix))
print(np.linalg.det(matrix))
