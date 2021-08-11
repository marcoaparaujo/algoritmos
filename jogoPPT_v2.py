from random import *

aposta_pessoa = int(input("Digite sua aposta (0=Pedra / 1=Papel / 2=Tesoura): "))
if aposta_pessoa < 0 or aposta_pessoa > 2:
    print("Aposta inválida")
else:
    aposta_computador = randint(0,2)
    if aposta_computador == 0:
        print("Jogada do computador: Pedra")
    else:
        if aposta_computador == 1:
            print("Jogada do computador: Papel")
        else:
            print("Jogada do computador: Tesoura")

    if aposta_pessoa == aposta_computador:
        print("Empate!!")
    else:
        if (aposta_pessoa == 0 and aposta_computador == 2) or (aposta_pessoa == 1 and aposta_computador == 0) or (aposta_pessoa == 2 and aposta_computador == 1):
            print("Você ganhou!!")
        else:
            print("Você perdeu!!")
