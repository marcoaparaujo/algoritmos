# Implemente uma função que retorne o maior elemento de um vetor de inteiros.

def retornar_maior_elemento(vetor):

    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior


vetor = [80, 10, 20, 4, 50, 2, 0, -1, 90]

print(f"Maior = {retornar_maior_elemento(vetor)}")