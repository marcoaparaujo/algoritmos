# Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir.
# Para cada número lido, mostre o valor lido e o fatorial deste valor.

qtde = int(input("Digite a quantidade de valores: "))

for i in range(1, qtde + 1):
    valor = int(input(f"Digite o valor {i}: "))
    fat = 1
    for j in range(1, valor + 1):
        fat *= j
    print(f"{valor}! = {fat}")
