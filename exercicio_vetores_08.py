# 8.	Implemente uma função que, dado um valor, retorne se esse valor pertence ou não a um vetor
# de inteiros.

def verificar_valor(vetor, valor):

    achou = False
    for i in range(len(vetor)):
        if vetor[i] == valor:
            achou = True
    return achou


vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(verificar_valor(vetor, 5))

