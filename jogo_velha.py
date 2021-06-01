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
    print(" "*4, end="")
    for i in range(dimensao):
        print(f"{i} ", end="")
    print()
    for i in range(dimensao):
        print(f"{i} [ ", end="")
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
        if linha == coluna:
            quantidade = 0
            for i in range(dimensao):
                if matriz[i][i] == jogador:
                    quantidade = quantidade + 1
            if quantidade == dimensao:
                ganhou = True

    if not ganhou:
        if coluna == dimensao - linha - 1:
            quantidade = 0
            for i in range(dimensao):
                if matriz[i][dimensao - i - 1] == jogador:
                    quantidade = quantidade + 1
            if quantidade == dimensao:
                ganhou = True

    return ganhou


dimensao = 3
max_jogadas = dimensao * dimensao
jogadores = ["X", "O"]

matriz = criar_matriz(dimensao)

proximo_jogador = randint(0, len(jogadores)-1)
jogador = jogadores[proximo_jogador]

ganhou = False
jogada = 1
exibir_matriz(matriz)
while not ganhou and jogada <= max_jogadas:

    jogada_ok = False
    while not jogada_ok:
        print(f"Jogador: {jogador}")
        linha = input(f"Digite a linha de 0 a {dimensao - 1}: ")
        coluna = input(f"Digite a coluna de 0 a {dimensao - 1}: ")

        if not linha.isnumeric() or not coluna.isnumeric():
            print("Dados inválidos")
        else:
            linha = int(linha)
            coluna = int(coluna)
            if linha < 0 or linha > dimensao - 1 or coluna < 0 or coluna > dimensao - 1:
                print("Coordenadas inválidas")
            else:
                if matriz[linha][coluna] == "_":
                    jogada_ok = True
                else:
                    print("Casa ocupada!")

    matriz[linha][coluna] = jogador
    exibir_matriz(matriz)

    if jogada >= dimensao * 2 - 1:
        if verificar_vencedor(matriz, linha, coluna, jogador):
            ganhou = True

    if not ganhou:
        jogada = jogada + 1
        if proximo_jogador == len(jogadores) - 1:
            proximo_jogador = 0
        else:
            proximo_jogador = proximo_jogador + 1
        jogador = jogadores[proximo_jogador]

if ganhou:
    print(f"{jogador} venceu!")
else:
    print("Velha!!")

