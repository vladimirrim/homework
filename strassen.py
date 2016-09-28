import numpy as np
import sys


def matrix_create():
    global n, a, b, k
    n = int(input(sys.stdin))
    k = 2
    while (k < n):
        k *= 2
    a = np.zeros((k, k))
    b = np.zeros((k, k))
    c = np.zeros((n + n, n))
    c[...] = np.loadtxt(sys.stdin)
    a[:n, :n] = c[:n, ].copy()
    b[:n, :n] = c[n:, ].copy()


def matrix_mull():
    a11 = a[:k // 2, :k // 2].copy()
    a12 = a[:k // 2, k // 2:].copy()
    a21 = a[k // 2:, :k // 2].copy()
    a22 = a[k // 2:, k // 2:].copy()
    b11 = b[:k // 2, :k // 2].copy()
    b12 = b[:k // 2, k // 2:].copy()
    b21 = b[k // 2:, :k // 2].copy()
    b22 = b[k // 2:, k // 2:].copy()
    I = np.dot((a11 + a22), (b11 + b22))
    II = np.dot((a21 + a22), b11)
    III = np.dot(a11, (b12 - b22))
    IV = np.dot(a22, (-b11 + b21))
    V = np.dot((a11 + a12), b22)
    VI = np.dot((a21 - a11), (b11 + b12))
    VII = np.dot((a12 - a22), (b21 + b22))
    c11 = I + IV - V + VII
    c21 = II + IV
    c12 = III + V
    c22 = I + III - II + VI
    c = np.zeros((k, k), dtype=int)
    c[:k // 2, :k // 2] = c11.copy()
    c[:k // 2, k // 2:] = c12.copy()
    c[k // 2:, :k // 2] = c21.copy()
    c[k // 2:, k // 2:] = c22.copy()
    c = c[:n, :n].copy()
    return c


def matrix_print(c):
    for i in range(n):
        for j in range(n):
            print(c[i, j], end=" ")

        print()


matrix_create()
matrix_mull()
matrix_print(matrix_mull())

