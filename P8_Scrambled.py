# Autor: Ángel Gabriel Aguillón Mora

def is_scramble(s1, s2, memo=None):
    if memo is None:
        memo = {}

    # Clave para memorizar el subproblema
    key = (s1, s2)
    if key in memo:
        return memo[key]

    # Si las cadenas son iguales, es válido
    if s1 == s2:
        memo[key] = True
        return True

    # Si las cadenas no tienen los mismos caracteres, no pueden ser scrambles
    if sorted(s1) != sorted(s2):
        memo[key] = False
        return False

    n = len(s1)
    for i in range(1, n):
        # Sin swap
        if is_scramble(s1[:i], s2[:i], memo) and is_scramble(s1[i:], s2[i:], memo):
            memo[key] = True
            return True
        # Con swap
        if is_scramble(s1[:i], s2[-i:], memo) and is_scramble(s1[i:], s2[:-i], memo):
            memo[key] = True
            return True

    memo[key] = False
    return False

# Ejemplos de prueba
print("Caso 1:", is_scramble("great", "rgeat"))  # True
print("Caso 2:", is_scramble("abcde", "caebd"))  # False
print("Caso 3:", is_scramble("a", "a"))          # True
