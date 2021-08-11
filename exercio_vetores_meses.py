nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
maximo_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def retornar_nome_mes(mes):
    if mes < 1 or mes > 12:
        return "Mês inválido"
    else:
        return nomes_meses[mes - 1]


def retornar_maximo_dias(mes):
    if mes < 1 or mes > 12:
        return "Mês inválido"
    else:
        return maximo_dias[mes - 1]


mes = int(input("Digite o número do mês: "))
print(f"Nome do mês = {retornar_nome_mes(mes)}")
print(f"Máximo dias = {retornar_maximo_dias(mes)}")
