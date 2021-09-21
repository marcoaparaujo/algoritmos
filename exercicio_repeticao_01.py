# Escrever um algoritmo que lê 10 valores e conte quantos destes valores são negativos,
# escrevendo esta informação.

qtdeNegativos = 0
qtdePositivos = 0
qtdeZeros = 0
quantidade = int(input("Digite a quantidade de valores: "))
for i in range(1, quantidade + 1):
    valor = int(input(f"Digite o valor {i}: "))
    if valor < 0:
        qtdeNegativos += 1
    else:
        if valor > 0:
            qtdePositivos += 1
        else:
            qtdeZeros += 1

print(f"Quantidade de negativos = {qtdeNegativos}")
print(f"Quantidade de positivos = {qtdePositivos}")
print(f"Quantidade de zeros = {qtdeZeros}")


