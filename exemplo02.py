
salario_bruto = float(input ("digite o salario bruto: "))
valor_hrextra = float(input ("digite o valor da hora extra: "))
qtd_hr = float(input("digite a quantidade de horas extras: "))
salario = salario_bruto + (qtd_hr * valor_hrextra)
inss = salario * 0.08
salario_liquido = salario - inss

print (salario_liquido)