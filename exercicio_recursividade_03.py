# Faça uma função recursiva para exibir os números compreendidos entre a e b, sendo a e b parâmetros da função.

def exibir_numeros_faixa(a, b):
    if a < b:
        exibir_numeros_faixa(a, b - 1)
    print(b)


exibir_numeros_faixa(10, 20)