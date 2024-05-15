#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for a in range(0, len(fila)):
            print("{:d}".format(fila[a]), end=" " if a < len(fila) - 1 else "")
        print()
