# 41.	Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos
#  a seguir. Para cada número lido, mostre o valor lido e o fatorial deste valor.  

quantidade = int(input("Quantos valores devem ser lidos? "))

for i in range(quantidade):
    numero = int(input("Digite um numero: "))

    fatorial = 1
    for contador in range(1, numero + 1):
        fatorial = fatorial * contador

    print(f"{numero}! = {fatorial}")

