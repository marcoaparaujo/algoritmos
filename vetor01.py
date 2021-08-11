meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Digite o numero do mes: "))
print(meses[mes-1])
print(dias[mes-1])