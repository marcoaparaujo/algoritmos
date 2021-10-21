# Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até n. Mostre a tabuada na forma:
# 1 x n = n
# 2 x n = 2n
# 3 x n = 3n
# ...............
# n x n = n2

n = int(input("Digite o valor de n: "))
for i in range(1, n + 1):
    print(f"{i} x {n} = {i * n}")

# n = int(input("Digite o valor de n: "))
# i = 1
# while i <= n:
#     print(f"{i} x {n} = {i * n}")
#     i += 1
