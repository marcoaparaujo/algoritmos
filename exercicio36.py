# Chico tem 1,50 metro e cresce 2 centímetros por ano,
# enquanto Zé tem 1,30 metro e cresce 3 centímetros por ano.
# Construa um algoritmo que calcule e imprima quantos anos serão
# necessários para que Zé seja maior que Chico.

altura_chico = 150
altura_ze = 130
qtde_anos = 0

while altura_ze <= altura_chico:
    altura_ze = altura_ze + 3
    altura_chico = altura_chico + 2
    qtde_anos = qtde_anos + 1

print(qtde_anos)
