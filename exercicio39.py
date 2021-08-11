numero = int(input("Digite um numero: "))

for contador in range(1, 11):
    print(f"{numero:2d} + {contador:2d} = {numero + contador:2d}        {numero:2d} - {contador:2d} = {numero - contador:2d}     {numero:2d} x {contador:2d} = {numero * contador:2d}     {numero:2d} / {contador:2d} = {numero / contador:.2f}")

