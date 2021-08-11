# 47.	Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a seguinte soma:  
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n 
# O algoritmo deve escrever cada termo gerado e o valor final de S.

numero = int(input("Digite um número: "))
if numero > 0:
    s = 0
    for i in range(1, numero + 1):
        termo = 1 / i
        print(f"Termo = {termo:.2f}")
        s = s + termo

    print(f"S = {s:.2f}")