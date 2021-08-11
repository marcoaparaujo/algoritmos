# Faça uma função recursiva para exibir na tela os números ímpares de 1 a 30.

def exibir_numeros_impares(num):
    if num != 1:
        exibir_numeros_impares(num - 2)
    print(num)

exibir_numeros_impares(29)