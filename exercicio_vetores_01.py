# Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores são negativos.

def contagem_negativa(numeros):
    contador_negativo = 0
    for i in range(len(numeros)):
        if numeros[i] < 0:
            contador_negativo = contador_negativo + 1
    return contador_negativo


numeros = []

for i in range(10):
    num = int(input("Digite um valor: "))
    numeros.append(num)

print(f"Existem {(contagem_negativa(numeros))} número negativos")
