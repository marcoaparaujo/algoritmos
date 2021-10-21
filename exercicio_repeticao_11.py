# Escrever um algoritmo que leia um número não determinado de valores e calcule a média aritmética
# dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o
# percentual de valores negativos e positivos. Mostre os resultados.

positivos = 0
negativos = 0

numero = int(input("Digite um número: "))
while numero != 0:
    if numero < 0:
        negativos += 1
    else:
        positivos += 1

    numero = int(input("Digite um número: "))

if positivos + negativos > 0:
    print(f"Total de positivos = {positivos}")
    print(f"Total de negativos = {negativos}")
    print(f"Percentual de positivos = {(positivos / (positivos + negativos)) * 100:.2f}%")
    print(f"Percentual de negativos = {(negativos / (positivos + negativos)) * 100:.2f}%")