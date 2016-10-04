import numpy as np


def matrix_create():
    n = int(input())
    k = 2
    while (k < n):
        k *= 2
    a = np.zeros((k, k))
    b = np.zeros((k, k))
    c = np.array([[j for j in input().split()] for i in range(2 * n)])
    a[:n, :n] = c[:n, ]
    b[:n, :n] = c[n:, ]
    return a, b, k, n


def matrix_mull(a, b, k, n):
    if k <= 1:
        return np.dot(a, b)
    else:
        k = k // 2
        a11 = a[:k, :k]
        a12 = a[:k, k:]
        a21 = a[k:, :k]
        a22 = a[k:, k:]
        b11 = b[:k, :k]
        b12 = b[:k, k:]
        b21 = b[k:, :k]
        b22 = b[k:, k:]
        I = matrix_mull(a11 + a22, b11 + b22, k, n)
        II = matrix_mull(a21 + a22, b11, k, n)
        III = matrix_mull(a11, b12 - b22, k, n)
        IV = matrix_mull(a22, b21 - b11, k, n)
        V = matrix_mull(a11 + a12, b22, k, n)
        VI = matrix_mull(a21 - a11, b11 + b12, k, n)
        VII = matrix_mull(a12 - a22, b21 + b22, k, n)

        c12 = III + V
        c21 = II + IV
        c11 = I + IV - V + VII
        c22 = I + III - II + VI

        c = np.zeros((2 * k, 2 * k))
        c[:k, :k] = c11
        c[:k, k:] = c12
        c[k:, :k] = c21
        c[k:, k:] = c22
        c = c[:n, :n]
        return c


def matrix_print(c):
    print('\n'.join([' '.join([str(i) for i in j]) for j in c]))


a, b, k, n = matrix_create()
matrix_print(matrix_mull(a, b, k, n))

