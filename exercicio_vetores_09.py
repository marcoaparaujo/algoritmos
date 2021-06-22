# 9.	Implemente uma função que retorne a média dos valores armazenados em um vetor de inteiros.


def calcular_media(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    if len(vetor) == 0:
        return 0
    else:
        return soma / len(vetor)


vetor = [3, 4, 2, 1, 8, 7]
print(calcular_media(vetor))
