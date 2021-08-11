# Faça uma função recursiva que receba um vetor de números inteiros e seu tamanho e retorne a soma de seus elementos.

def soma_vetor(vetor, tamanho):
    if tamanho == 0:
        return 0
    else:
        return vetor[tamanho - 1] + soma_vetor(vetor, tamanho - 1)



print(soma_vetor([1, 3, 4, 2], 4))

