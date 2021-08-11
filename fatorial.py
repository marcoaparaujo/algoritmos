def fatorial (numero):
    if (numero == 0):
        return 1
    else:
        return numero * fatorial(numero-1)

valor = int(input("Digite um valor: "))
print(fatorial(valor))

