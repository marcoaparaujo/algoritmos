# Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado.
# Funcionários com até 1 ano de empresa, receberão aumento de 10%. Funcionários com mais de um ano de tempo de serviço,
# receberão aumento de 20%.

salario = float(input("Digite o salário: "))
tempo_servico = int(input("Digite o tempo de serviço: "))

if tempo_servico <= 1:
    salario_reajustado = salario * 1.1
else:
    salario_reajustado = salario * 1.2

print(f"Salário Reajustado = R$ {salario_reajustado:.2f}")





