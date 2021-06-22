#	Escrever uma função que recebe por parâmetro um vetor de inteiros e o seu tamanho e
#	retorna a soma de seus elementos.

def retornar_soma(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]

    return soma

vetor = [80, 10, 20, 4, 50, 2, 0, -1, 90, 3, 2]

print(retornar_soma(vetor))
