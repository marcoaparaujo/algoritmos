# 44.	Faça um algoritmo que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos.
# O número que encerrará a leitura será zero.

qtde_pares = 0
qtde_impares = 0
soma_pares = 0
soma_geral = 0

numero = int(input("Digite um número: "))
while numero != 0:
    if numero > 0:
        soma_geral = soma_geral + numero

        if numero % 2 == 0:
            qtde_pares = qtde_pares + 1
            soma_pares = soma_pares + numero
        else:
            qtde_impares = qtde_impares + 1

    numero = int(input("Digite um número: "))

print(f"Quantidade de pares   = {qtde_pares}")
print(f"Quantidade de ímpares = {qtde_impares}")

if qtde_pares > 0:
    print(f"Média dos pares = {soma_pares / qtde_pares}")

qtde_geral = qtde_pares + qtde_impares
if qtde_geral > 0:
    print(f"Média geral = {soma_geral / qtde_geral}")
