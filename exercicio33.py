# Escreva um algoritmo que leia 20 valores e encontre o maior e o menor deles.
# Mostre o resultado.

contador = 0

while contador < 20:
    valor = int(input("Digite um valor: "))
    contador = contador + 1
    if contador == 1:
        maior = valor
        menor = valor
    else:
        if valor < menor:
            menor = valor
        else:
            if valor > maior:
                maior = valor

print(f"Maior = {maior} - Menor = {menor}")



