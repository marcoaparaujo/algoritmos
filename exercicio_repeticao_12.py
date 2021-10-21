# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes
# intervalos: [0,25], [26,50], [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um número negativo.

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0

numero = int(input("Digite um número: "))
while numero >= 0:
    if numero >= 0 and numero <= 25:
        faixa1 += 1
    else:
        if numero >= 25 and numero <= 50:
            faixa2 += 1
        else:
            if numero >= 51 and numero <= 75:
                faixa3 += 1
            else:
                if numero >= 76 and numero <= 100:
                    faixa4 += 1
    numero = int(input("Digite um número: "))

print(f"Quantidade de números no intervalo [ 0,  25] = {faixa1}")
print(f"Quantidade de números no intervalo [26,  50] = {faixa2}")
print(f"Quantidade de números no intervalo [51,  75] = {faixa3}")
print(f"Quantidade de números no intervalo [76, 100] = {faixa4}")
