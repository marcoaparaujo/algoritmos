# Calcular a média de combustível gasto pelo usuário, sendo informado a quantidade de
# quilômetros rodados e a quantidade de combustível consumido.

quilometros_rodados = int(input("Digite qa quantidade de quilometros rodados: "))
combustivel_consumido = int(input("Digite a quantidade de combustivel consumido: "))

consumo = quilometros_rodados / combustivel_consumido

print(f"Consumo Médio = {consumo:.2f} Km/l")