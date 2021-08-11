# Faça uma função recursiva para exibir na tela de 1 a 10.

def exibir_numero(num):
    if num != 1:
        exibir_numero(num - 1)
    print(num)


exibir_numero(10)
