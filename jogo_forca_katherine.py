#Verificar se a letra digitada esta dentro da palavra sorteada

#conta o numero de erros

#se chegar a 7 erros, enforcou

#para 19/10

import random

arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''
while len(palavra) < 5 or len(palavra) > 10:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
palavra = palavra.upper().strip()
arquivo.close()

print("######################## JOGO DA FORCA #########################")

print(palavra)

chances = 7
numErros = 0
palavraChute_correta = ""
palavraChute_errada = ""
palavraSaida = ""

print(f"A palavra tem {len(palavra)} letras! ")
chute = str(input("Digite seu chute: "))
chute = chute.upper().strip()
if len(chute) > 1:
    print("Digite somente uma letra por vez!")
else:
    palavraSaida = ""
    while palavraSaida != palavra and numErros < 7:
        if chute in palavraChute_correta or chute in palavraChute_errada:
            print("Você já chutou essa letra! Tente outra.")
        else:
            if chute in palavra:
                palavraChute_correta += chute
                palavraSaida = ""
                for letra in palavra:
                    if letra in palavraChute_correta:
                        palavraSaida += letra
                    else:
                        palavraSaida += "_"
                print(f"Correto! A palavra contém {chute}")
            else:
                palavraChute_errada += chute
                numErros += 1
                chances -= 1
                print("Chute errado!")
                if chances > 0:
                    print(f"Você ainda tem {chances} chances!")
            print(f"Acertos: {palavraSaida}")
        if palavra != palavraSaida and numErros < 7:
            chute = str(input("Digite seu chute: "))
            chute = chute.upper().strip()

    if numErros == 7:
        print("Você foi enforcado!")
        print(f"A palavra correta é {palavra}")
    else:
        print("Parabéns, você sobreviveu!")
        print(f"a palavra é {palavra}")












