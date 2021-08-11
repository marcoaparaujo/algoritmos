# 7.	Escrever uma função somar_intervalo(n1, n2) que retorna a soma  dos números inteiros que existem
# entre n1 e n2 (inclusive ambos). A função deve  funcionar inclusive se o valor de n2 for menor que n1.

def somar_intervalo(n1, n2):

    if n2 < n1:
        aux = n1
        n1 = n2
        n2 = aux

    soma = 0
    for numero in range(n1, n2 + 1):
        soma = soma + numero

    return soma


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print(f"Soma dos valores = {somar_intervalo(valor1, valor2)}")