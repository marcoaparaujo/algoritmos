adjacente = False
numero = int(input("Digite um numero: "))
resto_anterior = -1
while numero > 0:
    resto = numero % 10
    if resto == resto_anterior:
        adjacente = True
    numero = numero // 10
    resto_anterior = resto

if adjacente:
    print ("sim")
else:
    print("não")