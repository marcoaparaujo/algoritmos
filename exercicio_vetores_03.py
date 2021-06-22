# 3.	Implemente uma função que retorne o menor elemento de um vetor de inteiros.

def retornar_menor_elemento(vetor):

    menor = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor


vetor = [80, 10, 20, 4, 50, 2, 0, -1, 90]

print(f"Menor = {retornar_menor_elemento(vetor)}")