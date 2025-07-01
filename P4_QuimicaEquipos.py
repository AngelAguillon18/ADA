def dividir_jugadores(habilidades):
    habilidades.sort()  

    n = len(habilidades)
    suma_objetivo = habilidades[0] + habilidades[-1]
    suma_quimica = 0

    i = 0
    j = n - 1

    while i < j:
        if habilidades[i] + habilidades[j] != suma_objetivo:
            return -1  
        suma_quimica += habilidades[i] * habilidades[j]
        i += 1
        j -= 1

    return suma_quimica

print("Bienvenido. Este programa divide jugadores en equipos de 2 con habilidades iguales.")
entrada = input("Introduce las habilidades separadas por comas (por ejemplo: 3,2,5,1,3,4): ")

try:
    lista_habilidades = list(map(int, entrada.strip().split(",")))

    if len(lista_habilidades) % 2 != 0:
        print("El número de jugadores debe ser par.")
    else:
        resultado = dividir_jugadores(lista_habilidades)
        if resultado == -1:
            print("No es posible dividir a los jugadores en equipos con habilidades iguales.")
        else:
            print("La suma total de la química de todos los equipos es:", resultado)
except ValueError:
    print("Por favor, introduce solo números separados por comas.")
