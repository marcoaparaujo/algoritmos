quantidade = 0
numero = 1
while quantidade < 3:

    soma = 0;
    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i

    if soma == numero:
        print(numero)
        quantidade = quantidade + 1

    numero = numero + 1