# Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho
# (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado,
# reprovado ou se fará prova final. O aluno será reprovado se faltou mais de 15 aulas.
# Será aprovado se não for reprovado por falta e sua média for maior que 6,0.
# Caso tenha média menor, deverá fazer prova final.
# O cálculo da média deve ser feito com peso 3 para a primeira prova, 5 para a segunda prova e 2 para o trabalho.

nome = input("Digite o nome do aluno: ")
faltas = int(input("Digite o número de faltas: "))
if faltas < 0:
    print("Número de faltas inválido")
else:
    if faltas > 15:
        print("Aluno reprovado por infrequência")
    else:
        prova1 = float(input("Digite a nota da prova 1: "))
        if prova1 < 0 or prova1 > 10:
            print("Nota da prova 1 inválida")
        else:
            prova2 = float(input("Digite a nota da prova 2: "))
            if prova2 < 0 or prova2 > 10:
                print("Nota da prova 2 inválida")
            else:
                trabalho = float(input("Digite a nota do trabalho: "))
                if trabalho < 0 or trabalho > 10:
                    print("Nota do trabalho inválida")
                else:
                    media = ((prova1 * 3) + (prova2 * 5) + (trabalho * 2)) / 10
                    if media > 6.0:
                        print("Aluno aprovado")
                    else:
                        print("Aluno deve fazer prova final")


