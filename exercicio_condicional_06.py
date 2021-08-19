# Ler um número e informar se ele é positivo, negativo ou neutro (zero).

numero = int(input("Digite um número: "))

if numero < 0:
    print("Negativo")
else:
    if numero > 0:
        print("Positivo")
    else:
        print("Neutro")
