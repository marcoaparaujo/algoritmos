# Faça uma função que recebe, por parâmetro, uma matriz 7x6 e retorna a soma dos elementos
#  da linha 5 e da coluna 3.


def soma_linha(matriz, num_linha):
    soma = 0
    for j in range(len(matriz[0])):
        soma = soma + matriz[num_linha][j]
    return soma


def soma_coluna(matriz, num_coluna):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][num_coluna]
    return soma


matriz = [
    [1, 2, 3, 4, 5, 6],
    [6, 7, 8, 9, 0, 1],
    [2, 3, 4, 5, 6, 7],
    [7, 8, 9, 0, 1, 2],
    [2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8],
    [4, 5, 6, 7, 8, 9]
]

print(f"Soma da linha 5 com a coluna 3 = {soma_linha(matriz, 5) + soma_coluna(matriz, 3)}")

# soma da linha 5 = 33
# soma da coluna 3 = 36
# soma das duas = 69