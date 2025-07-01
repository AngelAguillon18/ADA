import random
import time

# Función para generar una matriz nxn aleatoria
def generar_matriz(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Método tradicional
def multiplicacion_tradicional(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Funciones auxiliares para DaC y Strassen
def sumar_matrices(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def restar_matrices(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def dividir_matriz(M):
    n = len(M)
    mitad = n // 2
    A11 = [row[:mitad] for row in M[:mitad]]
    A12 = [row[mitad:] for row in M[:mitad]]
    A21 = [row[:mitad] for row in M[mitad:]]
    A22 = [row[mitad:] for row in M[mitad:]]
    return A11, A12, A21, A22

def combinar_matrices(C11, C12, C21, C22):
    n = len(C11)
    C = []
    for i in range(n):
        C.append(C11[i] + C12[i])
    for i in range(n):
        C.append(C21[i] + C22[i])
    return C

# Divide and Conquer (DaC)
def multiplicacion_dac(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    A11, A12, A21, A22 = dividir_matriz(A)
    B11, B12, B21, B22 = dividir_matriz(B)
    C11 = sumar_matrices(multiplicacion_dac(A11, B11), multiplicacion_dac(A12, B21))
    C12 = sumar_matrices(multiplicacion_dac(A11, B12), multiplicacion_dac(A12, B22))
    C21 = sumar_matrices(multiplicacion_dac(A21, B11), multiplicacion_dac(A22, B21))
    C22 = sumar_matrices(multiplicacion_dac(A21, B12), multiplicacion_dac(A22, B22))
    return combinar_matrices(C11, C12, C21, C22)

# Strassen
def multiplicacion_strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    A11, A12, A21, A22 = dividir_matriz(A)
    B11, B12, B21, B22 = dividir_matriz(B)

    M1 = multiplicacion_strassen(sumar_matrices(A11, A22), sumar_matrices(B11, B22))
    M2 = multiplicacion_strassen(sumar_matrices(A21, A22), B11)
    M3 = multiplicacion_strassen(A11, restar_matrices(B12, B22))
    M4 = multiplicacion_strassen(A22, restar_matrices(B21, B11))
    M5 = multiplicacion_strassen(sumar_matrices(A11, A12), B22)
    M6 = multiplicacion_strassen(restar_matrices(A21, A11), sumar_matrices(B11, B12))
    M7 = multiplicacion_strassen(restar_matrices(A12, A22), sumar_matrices(B21, B22))

    C11 = sumar_matrices(restar_matrices(sumar_matrices(M1, M4), M5), M7)
    C12 = sumar_matrices(M3, M5)
    C21 = sumar_matrices(M2, M4)
    C22 = sumar_matrices(restar_matrices(sumar_matrices(M1, M3), M2), M6)
    return combinar_matrices(C11, C12, C21, C22)

# Tabla de resultados
def medir_tiempos():
    tamaños = [2, 4, 8, 16, 32, 64, 128, 256, 512]
    print(f"{'n':>5} | {'Tradicional (s)':>17} | {'DaC (s)':>10} | {'Strassen (s)':>13}")
    print("-" * 52)
    for n in tamaños:
        A = generar_matriz(n)
        B = generar_matriz(n)

        ini = time.perf_counter()
        multiplicacion_tradicional(A, B)
        tiempo_trad = time.perf_counter() - ini

        ini = time.perf_counter()
        multiplicacion_dac(A, B)
        tiempo_dac = time.perf_counter() - ini

        ini = time.perf_counter()
        multiplicacion_strassen(A, B)
        tiempo_strassen = time.perf_counter() - ini

        print(f"{n:>5} | {tiempo_trad:17.6f} | {tiempo_dac:10.6f} | {tiempo_strassen:13.6f}")

if __name__ == "__main__":
    medir_tiempos()
