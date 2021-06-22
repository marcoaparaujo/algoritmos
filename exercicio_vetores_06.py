# 6.	Escrever a função que recebe por parâmetro uma string e um número. A função deve retornar
#  os primeiros caracteres da string de acordo com o número passado por parâmetro.

def extrair_caracteres(string, numero):
    resposta = ''
    if numero > len(string):
        numero = len(string)
    for i in range(numero):
        resposta = resposta + string[i]
    return resposta


print(extrair_caracteres("UniAcademia", 3))
