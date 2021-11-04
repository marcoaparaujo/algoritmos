# Escrever um algoritmo que leia um valor N inteiro e positivo e que calcula o valor de E.
# Imprime o resultado de E ao final.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / N!

valor = int(input("Digite um valor: "))
if valor <= 0:
    print("Valor deve ser inteiro e positivo")
else:
    e = 1
    for i in range(1, valor + 1):
        fat = 1
        for j in range(1, i + 1):
            fat = fat * j

        e = e + (1 / fat)

    print(f"E = {e:.2f}")

# E = 1 + 1/1! + 1/2! + 1/3!
# E =  1 + 1 + 0.5 + 0.17