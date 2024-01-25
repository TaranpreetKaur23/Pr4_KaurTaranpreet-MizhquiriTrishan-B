import random

limitInferior = 0
limitSuperior = 50

# Generar una lista de 100 números aleatorios
numeros = [random.randint(limitInferior, limitSuperior) for _ in range(100)]

print("Números generados:", numeros)

# Filtrar números pares
numeros_pares = [num for num in numeros if num % 2 == 0]

# Calcular la media aritmética de los números pares
media_pares = sum(numeros_pares) / len(numeros_pares)

# Filtrar números impares
numeros_impares = [num for num in numeros if num % 2 != 0]
media_impares = sum(numeros_impares) / len(numeros_impares)


print("Números pares:", numeros_pares)
print(f"Media de números pares: {media_pares:.2f}")
print("Números impares:", numeros_impares)
print(f"Media de números impares: {media_impares:.2f}")