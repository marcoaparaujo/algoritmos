# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,30 metro e cresce 3 centímetros por ano.
# Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.

chico = 150
ze = 130
anos = 0
while ze <= chico:
    chico += 2
    ze += 3
    anos += 1
print(anos)
