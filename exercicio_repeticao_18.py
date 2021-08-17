# Escrever um algoritmo que gere e escreva os 3 primeiros números perfeitos.
# Um número perfeito é aquele que é igual a soma dos seus divisores.
# (Ex.: 6 = 1+2+3; 28= 1+2+4+7+14, etc).

quantidade = 0
numero = 1
while quantidade < 4:

    soma = 0
    for i in range(1, int(numero/2)+1):
        if numero % i == 0:
            soma = soma + i

    if soma == numero:
        print(numero)
        quantidade = quantidade + 1

    numero = numero + 1
