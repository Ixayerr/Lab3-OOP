import numpy as np


def process_matrix(file_name, K):
    "Обробляє матрицю з файлу, обчислює потрібні параметри."
    matrix = np.loadtxt(file_name, dtype=int)
    M, N = matrix.shape
    if not (1 <= K <= N):
        raise ValueError("K має бути в межах від 1 до N")

    column_sum = np.sum(matrix[:, K - 1])
    column_product = np.prod(matrix[:, K - 1])

    identity_matrix = np.eye(M, dtype=int)
    sum_matrix = matrix + identity_matrix

    return column_sum, column_product, sum_matrix


def matrix_task():
    "функція для виклику обробки матриці."
    file_name = input("Введіть ім'я файлу з матрицею: ")
    K = int(input("Введіть номер стовпця К: "))
    column_sum, column_product, sum_matrix = process_matrix(file_name, K)

    print(f"Сума елементів {K}-го стовпця: {column_sum}")
    print(f"Добуток елементів {K}-го стовпця: {column_product}")
    print("Сума матриці з одиничною матрицею:")
    print(sum_matrix)
