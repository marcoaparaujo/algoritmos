# Efetuar a leitura do número de quilowatts consumidos e calcular o valor a ser pago de energia elétrica,
# sabendo-se que o valor a pagar por quilowatt é de 0,12.
# Apresentar o valor total a ser pago pelo usuário acrescido de 18% de ICMS.

numero_quilowatts = int(input("Digite o número de quilowatts consumidos: "))

valor_pagar = (numero_quilowatts * 0.12) * 1.18

print(f"Valor total a pagar = R$ {valor_pagar:.2f}")
