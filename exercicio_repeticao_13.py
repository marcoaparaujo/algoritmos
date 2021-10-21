# Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a quantidade de
# números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a
# leitura será zero.

qtdePares = 0
qtdeImpares = 0
somaPares = 0
somaGeral = 0

numero = int(input("Digite um número: "))
while numero != 0:
    if numero > 0:
        somaGeral += numero
        if numero % 2 == 0:
            qtdePares += 1
            somaPares += numero
        else:
            qtdeImpares += 1

    numero = int(input("Digite um número: "))

print(f"Quantidade de pares = {qtdePares}")
print(f"Quantidade de ímpares = {qtdeImpares}")

if qtdePares > 0:
    print(f"Média dos pares = {somaPares / qtdePares}")

if qtdePares + qtdeImpares > 0:
    print(f"Média geral = {somaGeral / (qtdePares + qtdeImpares)}")