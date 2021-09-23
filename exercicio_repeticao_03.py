# Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial de N (N!).

valor = int(input("Digite um valor: "))
if valor <= 0:
    print("Valor inválido")
else:
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i

    print(f"{valor}! = {fatorial}")

