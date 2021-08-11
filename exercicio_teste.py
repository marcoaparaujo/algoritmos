from random import *

def exibir_matriz(matriz):
    print (" "*4, end="")
    for i in range(dimensao):
        print(f"{i} ", end="")
    print()

    for i in range(dimensao):
        print (f"{i} [ ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("]")
    print()

def verificar_vencedor(matriz, linha, coluna, jogador):
    ganhou = False

    quantidade = 0
    for j in range(dimensao):
        if matriz[linha][j] == jogador:
            quantidade = quantidade + 1
    if quantidade == dimensao:
        ganhou = True

    if not ganhou:
        quantidade = 0
        for i in range(dimensao):
            if matriz[i][coluna] == jogador:
                quantidade = quantidade + 1
        if quantidade == dimensao:
            ganhou = True

    if not ganhou:
        quantidade = 0
        for i in range(dimensao):
            if matriz[i][i] == jogador:
                quantidade = quantidade + 1
        if quantidade == dimensao:
            ganhou = True

    if not ganhou:
        quantidade = 0
        for i in range(dimensao):
            if matriz[i][dimensao-1-i] == jogador:
                quantidade = quantidade + 1
        if quantidade == dimensao:
            ganhou = True

    return ganhou

dimensao = 3
max_jogadas = dimensao * dimensao
matriz = []
for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        linha.append("_")
    matriz.append(linha)

sorteio = randint(0,1)
if sorteio == 0:
    jogador = "X"
else:
    jogador = "0"

ganhou = False
jogada = 1
exibir_matriz(matriz)
while not ganhou and jogada <= max_jogadas:
    print(f"Jogador: {jogador}")

    jogada_ok = False
    while not jogada_ok:
        linha = int(input(f"Digite a linha (0 a {dimensao - 1}): "))
        coluna = int(input(f"Digite a coluna (0 a {dimensao - 1}): "))
        if linha < 0 or linha > dimensao - 1 or coluna < 0 or coluna > dimensao - 1:
            print("Coordenadas invalidas")
        else:
            if matriz [linha][coluna] == "_":
                jogada_ok = True
            else:
                print("Casa já ocupada")

    matriz [linha][coluna] = jogador
    exibir_matriz(matriz)
    if verificar_vencedor(matriz, linha, coluna, jogador):
        ganhou = True
    else:
        jogada = jogada + 1
        if jogador == "X":
            jogador = "0"
        else:
            jogador = "X"

if ganhou:
    print(f"{jogador} venceu!")
else:
    print("Velha!")
