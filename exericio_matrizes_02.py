# Faça uma função que recebe, por parâmetro, uma matriz 6x6 e
# retorna a soma dos elementos da sua diagonal principal e da sua diagonal secundária.

def calcular_soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][i]
    return soma

def calcular_soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][len(matriz) - 1 - i]
    return soma

def calcular_soma_principal_secundaria(matriz):
    return calcular_soma_diagonal_principal(matriz) + calcular_soma_diagonal_secundaria(matriz)

matriz = [
    [1, 2, 3, 4, 5, 1],
    [6, 7, 8, 9, 0, 2],
    [2, 3, 4, 5, 6, 3],
    [7, 8, 9, 0, 1, 4],
    [2, 3, 4, 5, 6, 5],
    [3, 4, 5, 6, 7, 8],
]

print(f"Soma da diagonal principal = {calcular_soma_diagonal_principal(matriz)}")
print(f"Soma da diagonal secundaria = {calcular_soma_diagonal_secundaria(matriz)}")
print(f"Soma das duas diagonais = {calcular_soma_principal_secundaria(matriz)}")

# Soma da diagonal principal = 26
# Soma da diagonal secundaria = 21
# Soma das duas diagonais = 47

# Diagonal principal
# elemento 1 - i=0 / j=0  => i = j
# elemento 7 - i=1 / j=1  => i = j
# elemento 4 - i=2 / j=2  => i = j
# elemento 0 - i=3 / j=3  => i = j
# elemento 6 - i=4 / j=4  => i = j
# elemento 8 - i=5 / j=5  => i = j

# Diagonal secundária
# elemento 1 - i=0 / j=5  => i + j = 5
# elemento 0 - i=1 / j=4  => i + j = 5
# elemento 5 - i=2 / j=3  => i + j = 5
# elemento 9 - i=3 / j=2  => i + j = 5
# elemento 3 - i=4 / j=1  => i + j = 5
# elemento 3 - i=5 / j=0  => i + j = 5
# len (matriz) = 6 => len(matriz) - 1








