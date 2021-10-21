# Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:  
# 1,2,3,4 = voto para os respectivos candidatos;
# 5 = voto nulo;
# 6 = voto em branco.
#
# Elabore um algoritmo que leia o código do candidato em um voto. Calcule e escreva as seguintes informações:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco.
# Como finalizador do conjunto de votos, utilize o valor 0.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

voto = int(input("Digite seu voto: "))
while voto != 0:
    if voto == 1:
        candidato1 += 1
    else:
        if voto == 2:
            candidato2 += 1
        else:
            if voto == 3:
                candidato3 += 1
            else:
                if voto == 4:
                    candidato4 += 1
                else:
                    if voto == 5:
                        nulo += 1
                    else:
                        if voto == 6:
                            branco += 1
    voto = int(input("Digite seu voto: "))

print(f"Votos do candidato 1 = {candidato1}")
print(f"Votos do candidato 2 = {candidato2}")
print(f"Votos do candidato 3 = {candidato3}")
print(f"Votos do candidato 4 = {candidato4}")
print(f"Votos em branco = {branco}")
print(f"Votos nulos = {nulo}")

