# Faça uma função recursiva que receba um vetor de números inteiros e seu tamanho e retorne o menor elemento deste vetor.


def menor_valor(vetor, tamanho):

    if tamanho == 1:
        return vetor[0]

    menor = menor_valor(vetor, tamanho - 1)

    if vetor[tamanho - 1] < menor:
        return vetor[tamanho - 1]
    else:
        return menor


print(menor_valor([1, 3, 4, 0], 4))
