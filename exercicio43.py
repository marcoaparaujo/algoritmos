# 43.	Escrever um algoritmo que leia uma quantidade desconhecida de números e
# conte quantos deles estão nos seguintes intervalos:
# [0,25], [26,50], [51,75] e [76,100].
# A entrada de dados deve terminar quando for lido um número negativo.  


limite1 = 0
limite2 = 0
limite3 = 0
limite4 = 0
numero = int(input("Digite um numero: "))
while numero >= 0:
    if numero <= 25:
        limite1 = limite1 + 1
    else:
        if numero <= 50:
            limite2 = limite2 + 1
        else:
            if numero <= 75:
                limite3 = limite3 + 1
            else:
                if numero <= 100:
                    limite4 = limite4 + 1
    numero = int(input("Digite um numero: "))

print(f"Quantidade no limite 1: {limite1}")
print(f"Quantidade no limite 2: {limite2}")
print(f"Quantidade no limite 3: {limite3}")
print(f"Quantidade no limite 4: {limite4}")




