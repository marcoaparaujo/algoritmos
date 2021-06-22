from random import *

def criar_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append("_")
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    letra_inicial = 65
    print(" "*5, end="")
    for i in range(dimensao):
        print(f"{chr(letra_inicial + i)} ", end="")
    print()
    for i in range(dimensao):
        print(f"{i:2} [ ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("]")
    print()

def sortear_minas(matriz):
    dimensao = len(matriz)
    cont_minas = 0
    while cont_minas < dimensao:
        linha = randint(0, dimensao - 1)
        coluna = randint(0, dimensao - 1)
        if matriz[linha][coluna] != "M":
            matriz[linha][coluna] = "M"
            cont_minas = cont_minas + 1
    return matriz

def calcular_vizinhanca(matriz):
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(dimensao):

            if matriz[i][j] != "M":

                linha_inicial = i - 1
                if linha_inicial < 0:
                    linha_inicial = 0
                linha_final = i + 1
                if linha_final > dimensao - 1:
                    linha_final = dimensao - 1
                coluna_inicial = j - 1
                if coluna_inicial < 0:
                    coluna_inicial = 0
                coluna_final = j + 1
                if coluna_final > dimensao - 1:
                    coluna_final = dimensao - 1

                valor = 0
                for l in range(linha_inicial, linha_final + 1):
                    for c in range(coluna_inicial, coluna_final + 1):
                        if matriz[l][c] == "M":
                            valor = valor + 1
                if valor != 0:
                    matriz[i][j] = valor

    return matriz

def abrir_matriz(matriz, i, j):
    dimensao = len(matriz)

    if matriz[i][j] == "_":
        matriz[i][j] = " "

        linha_inicial = i - 1
        if linha_inicial < 0:
            linha_inicial = 0
        linha_final = i + 1
        if linha_final > dimensao - 1:
            linha_final = dimensao - 1
        coluna_inicial = j - 1
        if coluna_inicial < 0:
            coluna_inicial = 0
        coluna_final = j + 1
        if coluna_final > dimensao - 1:
            coluna_final = dimensao - 1

        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                abrir_matriz(matriz, l, c)


dimensao = 10

matriz = criar_matriz(dimensao)
matriz = sortear_minas(matriz)
matriz = calcular_vizinhanca(matriz)
exibir_matriz(matriz)
linha = int(input("Digite a linha: "))
coluna = input("Digite a coluna: ")
coluna = coluna.upper()
coluna = ord(coluna) - 65
abrir_matriz(matriz, linha, coluna)
exibir_matriz(matriz)
