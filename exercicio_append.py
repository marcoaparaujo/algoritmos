vetor = [2, 3, 1, 8, 6, 5]
vetor = [1, 2, 3, 8, 6, 5]
vetor = [1, 2, 3, 8, 6, 5]
vetor = [1, 2, 3, 5, 8, 6]
vetor = [1, 2, 3, 5, 6, 8]

def ordernar_vetor(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[i]:
                aux = vetor[i]
                vetor[i]=vetor[j]
                vetor[j]=aux
    return vetor

print(ordernar_vetor(vetor))



