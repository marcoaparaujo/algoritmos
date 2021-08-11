import random

def sortear_palavra():
    arquivo = open("br-sem-acentos.txt")
    linhas = arquivo.readlines()
    palavra = ''
    while len(palavra) < 5 or len(palavra) > 10:
        sorteio = random.randint(0, len(linhas))
        palavra = linhas[sorteio]
    palavra = palavra.upper()
    arquivo.close()
    return palavra


