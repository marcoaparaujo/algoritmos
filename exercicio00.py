vetor = [3, 8, 5, 1, 6, 7, 9, 2, 0, 4]
for ind1 in range (0, len(vetor)):
    for ind2 in range (ind1, len(vetor)):
        if vetor[ind2] < vetor[ind1]:
            aux = vetor[ind2]
            vetor[ind2] = vetor[ind1]
            vetor[ind1] = aux
print(vetor)