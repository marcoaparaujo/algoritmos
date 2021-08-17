# Calcular o salário líquido do funcionário sabendo que este é constituído pelo salário bruto
# mais o valor das horas extras subtraindo 8% de INSS do total.
# Serão lidos nesse problema o salário bruto, o valor das horas extras e o número de horas extras.
# Apresentar ao final o salário líquido.

salario_bruto = float(input("Digite o salário bruto: "))
valor_hora_extra = float(input("Digite o valor da hora extra: "))
numero_horas_extras = int(input("Digite o número de horas extras: "))

total_horas_extras = valor_hora_extra * numero_horas_extras
salario = salario_bruto + total_horas_extras
salario_liquido = salario * 0.92

print(f"Salário Líquido = R$ {salario_liquido:.2f}")



