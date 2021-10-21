import random

arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''
while len(palavra) < 5 or len(palavra) > 10:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
palavra = palavra.upper().strip()
arquivo.close()

print(palavra)
print("X" in palavra)


