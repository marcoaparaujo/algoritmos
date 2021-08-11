# 45.	Uma empresa deseja aumentar seus preços em 20%.
# Faça um algoritmo que leia o código e o preço de custo de cada produto e calcule o preço novo.
# Calcule também, a média dos preços com e sem aumento.
# Mostre o código e o preço novo de cada produto e, no final, as médias.
# A entrada de dados deve terminar quando for lido um código de produto negativo.


soma_preco_custo = 0
qtde_produtos = 0

codigo = int(input("Digite um código: "))
while codigo != 0:
    preco_custo = float(input("Digite o preço de custo: "))

    preco_novo = preco_custo * 1.2

    print(f"O novo preço do produto {codigo} = {preco_novo:.2f}")

    soma_preco_custo = soma_preco_custo + preco_custo
    qtde_produtos = qtde_produtos + 1

    codigo = int(input("Digite um código: "))

if qtde_produtos > 0:
    media_preco_custo = soma_preco_custo/qtde_produtos
    print(f"Média dos preços de custo = {media_preco_custo:.2f}")
    print(f"Média dos preços novos    = {media_preco_custo * 1.2:.2f}")
