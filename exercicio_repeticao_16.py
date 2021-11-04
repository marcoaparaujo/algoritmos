# Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a seguinte soma:
#
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
#
# O algoritmo deve escrever cada termo gerado e o valor final de S.

s = 0
n = int(input("Digite um número: "))

for i in range(1, n + 1):
    s += 1/i
    print(1/i)

print(f"S = {s}")
