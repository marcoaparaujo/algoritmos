notas = []

for i in range(5):
    aluno = []
    for j in range(3):
        nota = int(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        aluno.append(nota)

    notas.append(aluno)

for i in range(5):
    print(notas[i])

soma = 0
for i in range(5):
    for j in range(3):
        soma = soma + notas[i][j]

print(soma)
