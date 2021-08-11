
notas = []

nota = int(input("Digite uma nota: "))
while nota >= 0:
    notas.append(nota)
    nota = int(input("Digite uma nota: "))

print(notas)

soma = 0
for i in range(len(notas)):
    soma = soma + notas[i]

media = soma / len(notas)

print(media)

for i in range(len(notas)):
    if notas[i] > media:
        print(notas[i])

print(10 in notas)
print(notas.count(0))