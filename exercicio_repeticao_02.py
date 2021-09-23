# Escreva um algoritmo que leia 20 valores e encontre o maior e o menor deles. Mostre o resultado.

maior = 0
menor = 0

for i in range(1, 11):
    valor = int(input(f"Digite o valor {i}: "))
    if i == 1:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior valor = {maior}")
print(f"Menor valor = {menor}")

