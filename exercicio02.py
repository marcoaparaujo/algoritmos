from random import *
qtde = 0
saida = []
while qtde < 6:
    numero = randint(1,6)
    if numero not in saida:
        saida.append(numero)
        qtde = qtde + 1
print (saida)