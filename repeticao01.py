# Escrever um algoritmo que lê 10 valores e conte quantos destes valores são negativos, escrevendo esta informação.

negativos = 0
contador = 0
while contador < 10:
    numero = int(input(f"Digite o numero {contador + 1}: "))
    if numero < 0:
        negativos = negativos + 1
    contador = contador + 1

if negativos == 0:
    print("Não existem números negativos")
else:
    if negativos == 1:
        print("Existe 1 número negativo")
    else:
        print(f"Existem {negativos} números negativos")

