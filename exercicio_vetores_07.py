# 7.	Escrever a função que recebe por parâmetro uma string e um caracter.
# e a função deve retornar os primeiros caracteres da string até encontrar o caracter passado por parâmetro.

def extrair_primeiros_caracteres(string, letra):
    resposta = ''
    i = 0
    achou_letra = False
    while i < len(string) and not achou_letra:
        if string[i] == letra:
            achou_letra = True
        else:
            resposta = resposta + string[i]
        i = i + 1

    return resposta

print(extrair_primeiros_caracteres("UniAcademia", "A"))

