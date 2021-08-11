dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def exibir_dias_meses():
    for i in range(12):
        print(dias[i])

def exibir_dias_mes(mes):
    print(dias[mes])

def retornar_dias_mes(mes):
    return dias[mes]

mes = 0
while mes < 1 or mes > 12:
    mes = int(input("Digite o mes: "))

exibir_dias_meses()
exibir_dias_mes(mes-1)
print(retornar_dias_mes(mes-1))

