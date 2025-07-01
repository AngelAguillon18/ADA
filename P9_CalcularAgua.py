def calcular_agua_atrapada(alturas):
    """
    Calcula cuánta agua se puede atrapar entre las barras después de llover.

    :param alturas: Lista de enteros que representan las alturas de las barras
    :return: Entero que indica la cantidad total de agua atrapada
    """
    if not alturas or len(alturas) < 3:
        return 0  # No se puede atrapar agua con menos de 3 barras

    n = len(alturas)
    max_izquierda = [0] * n
    max_derecha = [0] * n

    # Calcular alturas máximas hacia la izquierda
    max_izquierda[0] = alturas[0]
    for i in range(1, n):
        max_izquierda[i] = max(max_izquierda[i - 1], alturas[i])

    # Calcular alturas máximas hacia la derecha
    max_derecha[n - 1] = alturas[n - 1]
    for i in range(n - 2, -1, -1):
        max_derecha[i] = max(max_derecha[i + 1], alturas[i])

    # Calcular agua atrapada
    agua_total = 0
    for i in range(n):
        agua_en_posicion = min(max_izquierda[i], max_derecha[i]) - alturas[i]
        agua_total += agua_en_posicion

    return agua_total


# -------------------
# Ejecución de ejemplos
# -------------------

ejemplo_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ejemplo_2 = [4, 2, 0, 3, 2, 5]

print("Ejemplo 1:")
print("Entrada:", ejemplo_1)
print("Agua atrapada:", calcular_agua_atrapada(ejemplo_1))  # Salida esperada: 6

print("\nEjemplo 2:")
print("Entrada:", ejemplo_2)
print("Agua atrapada:", calcular_agua_atrapada(ejemplo_2))  # Salida esperada: 9
