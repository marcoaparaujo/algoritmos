def calcular_fatorial(numero):
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1
    return fatorial

qtde = 1
saida = 1
numero = int(input("Digite um numero: "))
while qtde <= numero:
    saida = saida + 1/calcular_fatorial(qtde)
    qtde = qtde + 1
print(saida)

