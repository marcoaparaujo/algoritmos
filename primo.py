numero=int(input("Digite um numero: "))
cont = 2
qtde = 0
while cont < numero:
    if numero % cont == 0:
        qtde = qtde + 1
    cont = cont + 1
if qtde == 0:
    print("Numero é primo")
else:
    print("Numero não é primo")
