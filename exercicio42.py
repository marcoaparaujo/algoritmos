# 42.	Escrever um algoritmo que leia um número não determinado de valores
# e calcule a média aritmética dos valores lidos, a quantidade de valores positivos,
# a quantidade de valores negativos e o percentual de valores negativos e positivos.
# Mostre os resultados.

qtde_zeros = 0
qtde_positivos = 0
qtde_negativos = 0
soma = 0

resposta = 's'
while resposta == 'S' or resposta == 's':
    valor = int(input('Digite um valor: '))
    soma = soma + valor
    if valor < 0:
        qtde_negativos = qtde_negativos + 1
    else:
        if valor > 0:
            qtde_positivos = qtde_positivos + 1
        else:
            qtde_zeros = qtde_zeros + 1

    resposta = input('Deseja continuar? (S/N) ')

total = qtde_negativos + qtde_positivos + qtde_zeros
if total > 0:
    print(f"Média = {soma / total:.2f}")

print(f"Quantidade de positivos = {qtde_positivos}")
print(f"Quantidade de negativos = {qtde_negativos}")

print(f"Percentual de positivos = {(qtde_positivos / total) * 100:.2f}%")
print(f"Percentual de negativos = {(qtde_negativos / total) * 100:.2f}%")

