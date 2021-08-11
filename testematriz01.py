matriz = []
num_linhas = 3
num_colunas = 3
for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        valor = int(input(f"Digite o valor da posicao {i}, {j}: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(num_linhas):
    print(f"{matriz[i]}")

soma = 0
for i in range(num_colunas):
    soma = soma + matriz[2][i]
print(f"Soma da linha 2 = {soma}")

soma = 0
for i in range(num_linhas):
    soma = soma + matriz[i][0]
print(f"Soma da coluna 0 = {soma}")

soma = 0
for i in range(num_linhas):
    soma = soma + matriz [i][i]
print(f"Soma da diagonal principal = {soma}")


