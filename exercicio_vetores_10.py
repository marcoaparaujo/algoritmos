# 10.	Escrever uma função que substitui por zero todos os números negativos do vetor passado por parâmetro,

def substituir_negativos(vetor):

    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0

    return vetor


vetor = [1, 3, 5, -1, 8, -3, 0]
print(substituir_negativos(vetor))

