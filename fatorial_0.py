def fatorial (numero):
    resposta = 1
    for i in range(1,numero+1):
        resposta = resposta * i
    return resposta

valor = int(input("Digite um valor: "))
print(fatorial(valor))

