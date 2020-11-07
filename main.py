import numpy as np
import math


def derterminant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    if len(matrix) == 1:
        return matrix[0][0]

    all_matrix = []

    for i in range(len(matrix)):
        new_matrix = []
        for j in range(1, len(matrix)):
            new_matrix.append([])
            for k in range(0, len(matrix)):
                if k == i:
                    pass
                # print(j)
                else:
                    new_matrix[j-1].append(matrix[j][k])

        all_matrix.append(new_matrix)

    sum = 0

    for i in range(len(all_matrix)):
        sum += matrix[0][i] * derterminant(all_matrix[i]) * ((-1)**i)

    return sum


def inverse(Matrix):
    new_matrix=[]

    for i in range(len(Matrix)):
        new_matrix.append([])
        for j in range(len(Matrix)):
            matrix_detriminant = []
            for k in range(len(Matrix)):
                if k != i:
                    matrix_detriminant.append([])
                    for l in range(len(Matrix)):
                        if j != l:
                            matrix_detriminant[len(matrix_detriminant) - 1].append(Matrix[l][k])

            new_matrix[i].append((derterminant(matrix_detriminant) * ((-1) ** (i+j))) / derterminant(Matrix))

    return new_matrix


def matrix_mult(matrix_1, matrix_2):
    new_matrix = []

    for i in range(len(matrix_1)):
        new_matrix.append([])
        for j in range(len(matrix_2[0])):
            skalar = 0

            for k in range(len(matrix_1[0])):
                skalar += matrix_1[i][k] * matrix_2[k][j]

            new_matrix[i].append(skalar)

    return new_matrix


def make_rotation_matrix(n, angel):
    rotation_matrix = []

    for i in range(n):
        rotation_matrix.append([])
        for j in range(n):
            if i == j:
                rotation_matrix[i].append(1)
            else:
                rotation_matrix[i].append(0)

    rotation_matrix[0][0] = math.cos(angel)
    rotation_matrix[1][1] = math.cos(angel)
    rotation_matrix[0][1] = math.sin(angel)
    rotation_matrix[1][0] = - math.sin(angel)


    return rotation_matrix


def rotation_vector(matrix, angel):
    rotation_matrix = make_rotation_matrix(len(matrix), angel)
    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([])
        skale = 0
        for j in range(len(matrix)):
            skale += matrix[j] + rotation_matrix[i][j]

        new_matrix[i].append(skale)

    return new_matrix



matrix_1 = [[1, 2], [1, 2]]
matrix = [[1, 2, 3, 4], [0, 4, 5, 6], [1, 0, 6, 9], [2, 1, 3, 4]]
print(derterminant(matrix))
print(np.linalg.det(matrix))
print(inverse(matrix))
print(np.linalg.inv(matrix))
a = [[1, 2, 4],  [2, 0, 3]]
b = [[2, 5], [1, 3], [1, 1]]
print(matrix_mult(a, b))
print(make_rotation_matrix(4, 100))
print('/////////')
print(rotation_vector([1, 1], 30))