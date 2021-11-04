# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
# e retorna essa idade expressa em dias.

def calcularDias (a, m, d):
    resultado = (a * 365) + (m * 30) + d
    return resultado

anos = int(input("Quantos anos inteiros vc tem? "))
meses = int(input("E quantos meses completos? "))
dias = int(input("E quantos dias? "))
resposta = calcularDias(anos, meses, dias)
print(f"Sua idade em dias = {resposta}")





