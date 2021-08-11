# Faça uma função que recebe, por parâmetro, uma matriz 5x5 e retorna a soma dos seus elementos.

def soma_elementos(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    return soma

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
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [2, 3, 4, 5, 6],
    [7, 8, 9, 0, 1],
    [2, 3, 4, 5, 6]
]
print(f"Soma dos elementos da matriz = {soma_elementos(matriz)}")

linha = 4
print(f"Soma dos elementos da linha {linha} da matriz = {soma_linha(matriz, linha)}")

coluna = 4
print(f"Soma dos elementos da coluna {coluna} da matriz = {soma_coluna(matriz, coluna)}")

print(f"Número de linhas da matriz = {len(matriz)}")
print(f"Número de colunas da matriz = {len(matriz[0])}")


