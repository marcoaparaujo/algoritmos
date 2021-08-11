# Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial de N

n = int(input("Digite um número inteiro e positivo: "))
if n < 0:
    print("Número inválido para cálculo de fatorial")
else:
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    print(f"O fatorial = {fatorial}")

