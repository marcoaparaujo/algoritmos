from random import *

aposta_computador = randint(0, 2)
aposta_pessoa = int(input("Digite sua aposta (0=Pedra / 1=Papel / 2=Tesoura): "))
if aposta_pessoa < 0 or aposta_pessoa > 2:
    print("Aposta inválida")
elif aposta_pessoa == aposta_computador:
    print("Empate!!")
elif aposta_pessoa == 0 and aposta_computador == 1:
    print("Você perdeu!! Você jogou Pedra e o computador jogou Papel")
elif aposta_pessoa == 0 and aposta_computador == 2:
    print("Você ganhou!! Você jogou Pedra e o computador jogou Tesoura")
elif aposta_pessoa == 1 and aposta_computador == 0:
    print("Você ganhou!! Você jogou Papel e o computador jogou Pedra")
elif aposta_pessoa == 1 and aposta_computador == 2:
    print("Você perdeu!! Você jogou Papel e o computador jogou Tesoura")
elif aposta_pessoa == 2 and aposta_computador == 0:
    print("Você perdeu!! Você jogou Tesoura e o computador jogou Pedra")
elif aposta_pessoa == 2 and aposta_computador == 1:
    print("Você ganhou!! Você jogou Tesoura e o computador jogou Papel")

