def is_palindrome(x):
    operaciones = 0  # Lo usaremos para contar las operaciones realizadas 

    # Esta funcion va a validar los casos especiales, com lo son números negativos o terminados en 0 (excepto el 0 mismo)
    if x < 0 or (x % 10 == 0 and x != 0):
        operaciones += 2
        return False, operaciones

    revertido = 0

    # Invertiremos la mitad del número para posteriormente compararlo
    while x > revertido:
        revertido = revertido * 10 + x % 10  # Agregar el último dígito a "revertido"
        x //= 10  # Eliminar el último dígito de "x"
        operaciones += 3  # Contar las 3 operaciones anteriores

    # Verificar si es un palíndromo (para números con longitud par o impar)
    resultado = (x == revertido or x == revertido // 10)
    operaciones += 2  # Dos operaciones ya que realiza la igualdad y división

    return resultado, operaciones

# Aqui se ingresa el numero que se desea saber si es polindromo o no 
try:
    numero = int(input("Ingresa un número entero: "))
    es_palindromo, total_operaciones = is_palindrome(numero)

    # Imprimimos los resultados
    print(f"¿Es {numero} un palíndromo?: {es_palindromo}")
    print(f"Número de operaciones realizadas: {total_operaciones}")

except ValueError:
    print("Por favor, ingresa un número entero válido.")


#Realizado por Aguillon Mora Angel Gabriel