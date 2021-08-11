def exibir_notas(max, notas, media):
    resultado = []
    for i in range(max):
        if notas[i] > media:
            resultado.append(notas[i])
    return resultado

soma = 0
notas = []
max = 5
for i in range(max):
    nota = int(input("Digite a nota: "))
    notas.append(nota)
    soma = soma + nota
media = soma/max
print(media)
print(exibir_notas(max, notas, media))

