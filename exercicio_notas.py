# Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho
# (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado,
# reprovado ou se fará prova final. O aluno será reprovado se faltou mais de 15 aulas.
# Será aprovado se não for reprovado por falta e sua média for maior que 6,0.
# Caso tenha média menor, deverá fazer prova final.
# O cálculo da média deve ser feito com peso 3 para a primeira prova, 5 para a segunda prova e 2 para o trabalho.
# Caso a prova final seja maior ou igual que 5, o aluno estará aprovado, senão estará reprovado

nome = input("Digite o nome do aluno: ")
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
trabalho = int(input("Digite a nota do trabalho: "))
faltas = int(input("Digite a quantidade de faltas: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or trabalho < 0 or trabalho > 10:
    print("Voce digitou uma nota invalida")
else:
    if faltas > 15:
        print("Reprovado por infrequencia")
    else:
        media = ((nota1 * 3) + (nota2 * 5) + (trabalho * 2)) / 10
        if media >= 6:
            print("Aprovado")
        else:
            final = int(input("Digite a nota da prova final: "))
            if final >= 5:
                print("Aprovado na prova final")
            else:
                print("Reprovado na prova final")





