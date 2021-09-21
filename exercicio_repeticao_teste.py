numAlunos = int(input("Quantos alunos tem na turma? "))
soma = 0
for i in range(1, numAlunos + 1):
    nota = int(input(f"Digite a nota final do aluno {i}: "))
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
    soma += nota

print(f"Média da Turma = {soma / numAlunos:.2f}")