# Escrever um algoritmo que lê 10 valores, um de cada vez, e conte quantos deles estão no intervalo [10,20]
# e quantos deles estão fora do intervalo, escrevendo estas informações.

qtdeIntervalo = 0

for i in range (1, 11):
    valor = int(input("Digite um valor: "))
    if valor >= 10 and valor <= 20:
        qtdeIntervalo += 1

print(f"Quantidade de valores dentro do intervalo [10, 20] = {qtdeIntervalo}")
print(f"Quantidade de valores fora do intervalo [10, 20]   = {10 - qtdeIntervalo}")
