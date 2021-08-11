# 48.	Escrever um algoritmo que lê 10 valores, um de cada vez, e conte quantos deles estão no intervalo [10,20]
# e quantos deles estão fora do intervalo, escrevendo estas informações.

dentro_intervalo = 0

for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    if valor >= 10 and valor <= 20:
        dentro_intervalo = dentro_intervalo + 1

print(f"Dentro do intervalo [10,20] = {dentro_intervalo} ")
print(f"Fora   do intervalo [10,20] = {10 - dentro_intervalo}")
