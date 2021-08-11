import random

arq = open("br-sem-acentos.txt")
linhas = arq.readlines()
print(len(linhas))

palavra = ''
while len(palavra) < 5:
    sorteio = random.randint(0,len(linhas)) + 1
    palavra = linhas[sorteio]

print(palavra.upper())

#for linha in linhas:
#    print(linha)

arq.close()