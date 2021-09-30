# Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos,
# digitados pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.

#
# Usando while com flag (valor negativo digitado pelo usuário)
#
soma = 0
qtde = 0
numero = int(input("Digite um número: "))
while numero >= 0:
    soma += numero
    qtde += 1
    numero = int(input("Digite um número: "))

if qtde > 0:
    print(f"Média = {soma/qtde:.2f}")

#
# Usando for (usuário teve que indicar o número de execuções)
#
soma = 0
qtde = int(input("Digite a quantidade de vezes a executar: "))
for i in range(1, qtde + 1):
    numero = int(input("Digite um número: "))
    soma += numero

if qtde > 0:
    print(f"Média = {soma / qtde:.2f}")

#
# Usando while com o mesmo comportamento do for (usuário teve que indicar o número de execuções)
#
soma = 0
i = 1
qtde = int(input("Digite a quantidade de vezes a executar: "))
while i <= qtde:
    numero = int(input("Digite um número: "))
    soma += numero
    i += 1

if qtde > 0:
    print(f"Média = {soma / qtde:.2f}")

#
# Usando while com o usuário informando se deseja continuar
#
soma = 0
qtde = 0
continuar = "S"
while continuar == "S":
    numero = int(input("Digite um número: "))
    soma += numero
    qtde += 1
    continuar = ""
    while continuar != "S" and continuar != "N":
        continuar = input("Deseja continuar(S/N)? ")
        continuar = continuar.upper()

if qtde > 0:
    print(f"Média = {soma/qtde:.2f}")

