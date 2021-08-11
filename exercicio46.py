# 46.	Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que divididos por 11 dão resto igual a 5.

for numero in range(1000, 2000):
    if numero % 11 == 5:
        print(numero)


num = 1000
while num < 2000:
    if num % 11 == 5:
        print(f"{num}")
    num = num + 1