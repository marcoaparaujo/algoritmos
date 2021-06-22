# Implemente uma função que ordene um vetor de inteiros de tamanho 10.

def ordenar(vetor):

    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[i]:
                aux = vetor[j]
                vetor[j] = vetor[i]
                vetor[i] = aux
    return vetor


vetor = [80, 10, 20, 4, 50, 2, 0, -1, 90, 3]

print(ordenar(vetor))
