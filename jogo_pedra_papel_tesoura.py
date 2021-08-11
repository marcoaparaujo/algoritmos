from random import *

vitorias_pessoa = 0
vitorias_computador = 0
num_partidas = 0

while vitorias_pessoa != 2 and vitorias_computador != 2 and num_partidas < 3:
    aposta_pessoa = int(input("Digite sua aposta (0=Pedra / 1=Papel / 2=Tesoura): "))
    if aposta_pessoa < 0 or aposta_pessoa > 2:
        print("Aposta inválida")
    else:
        num_partidas = num_partidas + 1
        aposta_computador = randint(0,2)
        if aposta_pessoa == aposta_computador:
            print("Empate!!")
        else:
            if aposta_pessoa == 0 and aposta_computador == 1:
                print("Você perdeu!! Você jogou Pedra e o computador jogou Papel")
                vitorias_computador = vitorias_computador + 1
            else:
                if aposta_pessoa == 0 and aposta_computador == 2:
                    print("Você ganhou!! Você jogou Pedra e o computador jogou Tesoura")
                    vitorias_pessoa = vitorias_pessoa + 1
                else:
                    if aposta_pessoa == 1 and aposta_computador == 0:
                        print("Você ganhou!! Você jogou Papel e o computador jogou Pedra")
                        vitorias_pessoa = vitorias_pessoa + 1
                    else:
                        if aposta_pessoa == 1 and aposta_computador == 2:
                            print("Você perdeu!! Você jogou Papel e o computador jogou Tesoura")
                            vitorias_computador = vitorias_computador + 1
                        else:
                            if aposta_pessoa == 2 and aposta_computador == 0:
                                print("Você perdeu!! Você jogou Tesoura e o computador jogou Pedra")
                                vitorias_computador = vitorias_computador + 1
                            else:
                                if aposta_pessoa == 2 and aposta_computador == 1:
                                    print("Você ganhou!! Você jogou Tesoura e o computador jogou Papel")
                                    vitorias_pessoa = vitorias_pessoa + 1

if vitorias_pessoa == vitorias_computador:
    print("Houve empate!!")
else:
    if vitorias_pessoa > vitorias_computador:
        print("Você ganhou a melhor de 3!!")
    else:
        print("Computador ganhou a melhor de 3!!")


