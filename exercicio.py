vetor=[]
soma = 0
qtde_notas = 4
for cont in range(qtde_notas):
    nota = float(input(f"Digite a nota {cont + 1}: "))
    vetor.append(nota)
    soma = soma + nota
media = soma / qtde_notas
print(f"Media = {media}")
for cont in range(len(vetor)):
    if vetor[cont] > media:
        print(vetor[cont])

