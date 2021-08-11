# 5.	Escrever uma função verificar_estacao(dia, mes), que retorna qual a estação do ano
#  da data passada por parâmetro. Lembrando que a primavera começa no dia 23 de setembro,
#  o verão em 21 de dezembro, o outono em 21 de  março e o inverno em 21 de junho.

def verificar_estacao(dia, mes):
    if dia < 1 or dia > 31 or mes < 1 or mes > 12:
        estacao = 'Digite um dia/mês valido'
    else:
        if (mes == 9 and dia >= 23) or mes == 10 or mes == 11 or (mes == 12 and dia < 21):
            estacao = 'Primavera'
        else:
            if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia < 21):
                estacao = 'Verão'
            else:
                if (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia < 21):
                    estacao = 'Outono'
                else:
                    if (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia < 23):
                        estacao = 'Inverno'
    return estacao

dia = int(input('Que dia é hoje? '))
mes = int(input('De qual mês? (em numeral) '))
print(verificar_estacao(dia, mes))


