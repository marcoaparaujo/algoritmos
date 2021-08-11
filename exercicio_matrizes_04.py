# Faça uma função que recebe, por parâmetro, uma matriz 6x6 e
# retorna o menor elemento da sua diagonal secundária.


def menor_elemento_diagonal_secundaria(matriz):
    menor = matriz[0][len(matriz) - 1]
    for i in range(len(matriz)):
        if matriz[i][len(matriz) - 1 - i] < menor:
            menor = matriz[i][len(matriz) - 1 - i]
    return menor


matriz = [
    [1, 2, 3, 4, 5, 8],
    [6, 7, 8, 9, 4, 2],
    [2, 3, 4, 5, 6, 3],
    [7, 8, 9, 0, 1, 4],
    [2, 3, 4, 5, 6, 5],
    [3, 4, 5, 6, 7, 8],
]

print(f"Menor elemento da diagonal secundária = {menor_elemento_diagonal_secundaria(matriz)}")
