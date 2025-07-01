# Autor: Ángel Gabriel Aguillón Mora

# Lista de objetos (nombre, peso, valor)
objetos = [
    ("Guitarra", 1, 1500),
    ("Estéreo",  4, 3000),
    ("Laptop",   3, 2000),
    ("iPhone",   1, 2000)
]

capacidad = 4
n = len(objetos)

# Crear matriz dp de (n+1) x (capacidad+1)
dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

# Llenar la tabla dp
for i in range(1, n + 1):
    nombre, peso, valor = objetos[i - 1]
    for w in range(1, capacidad + 1):
        if peso <= w:
            dp[i][w] = max(dp[i - 1][w], valor + dp[i - 1][w - peso])
        else:
            dp[i][w] = dp[i - 1][w]

# Mostrar matriz de valores
print("Matriz DP (valores máximos acumulados):")
for fila in dp:
    print(fila)

# Reconstruir los objetos elegidos
w = capacidad
res = dp[n][w]
objetos_elegidos = []

for i in range(n, 0, -1):
    if res <= 0:
        break
    if res != dp[i - 1][w]:
        nombre, peso, valor = objetos[i - 1]
        objetos_elegidos.append(nombre)
        res -= valor
        w -= peso

# Resultados
print("\nValor máximo posible:", dp[n][capacidad])
print("Objetos seleccionados:", objetos_elegidos)
