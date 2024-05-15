#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for a in range(len(matrix[i])):
            newmatrix[i][a] = matrix[i][a] ** 2
    return newmatrix
