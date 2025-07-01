# Autor: Ángel Gabriel Aguillón Mora

# Función para verificar si una posición es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generar secuencia de Fibonacci modificada (omitimos posiciones primas)
def fibonacci_filtrado(k):
    secuencia = []
    a, b = 0, 1
    pos = 1
    while a <= k:
        if not es_primo(pos):
            secuencia.append(a)
        a, b = b, a + b
        pos += 1
    return secuencia

# Estrategia codiciosa para encontrar los términos mínimos que suman K
def min_fibonacci_suma(k, secuencia):
    resultado = []
    i = len(secuencia) - 1
    while k > 0 and i >= 0:
        if secuencia[i] <= k:
            resultado.append(secuencia[i])
            k -= secuencia[i]
        i -= 1
    return resultado

# 1. Input personalizado
# Ejemplo: fecha de nacimiento = 25/12/1995
dia = 25
mes = 12
anio = 1995
K = dia * 100 + mes * 10 + (anio % 100)  # K = 2715

# 2. Generar secuencia filtrada
secuencia = fibonacci_filtrado(K)

# 3. Calcular solución óptima
solucion = min_fibonacci_suma(K, secuencia)

# 4. Mostrar resultados
print("Valor de K:", K)
print("Secuencia de Fibonacci filtrada:")
print(secuencia)
print("\nTérminos que suman K de forma óptima:")
print(" + ".join(map(str, solucion)), "=", sum(solucion))
print("Número mínimo de términos:", len(solucion))
