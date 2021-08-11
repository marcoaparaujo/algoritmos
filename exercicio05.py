def ordenar(vetor):
    for ind1 in range(0, len(vetor)):
        for ind2 in range(ind1, len(vetor)):
            if vetor[ind2] < vetor[ind1]:
                aux = vetor[ind2]
                vetor[ind2] = vetor[ind1]
                vetor[ind1] = aux
        print(vetor)
    return vetor

vetor = [10, 7, 3, 2, 20, 15, 0, 1, 18, 4]
print(ordenar(vetor))


