# Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que divididos por 11 dão
# resto igual a 5.

for numero in range(1000, 2000):
    if numero % 11 == 5:
        print(numero)
