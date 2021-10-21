# Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o código e o preço de custo de
# cada produto e calcule o preço novo. Calcule também, a média dos preços com e sem aumento. Mostre o código e o
# preço novo de cada produto e, no final, as médias. A entrada de dados deve terminar quando for lido um código de
# produto negativo.

somaPrecos = 0
qtdeProdutos = 0

codigo = int(input("Digite um código de produto: "))
while codigo >= 0:
    preco = float(input("Digite o preço do produto: "))
    somaPrecos += preco
    qtdeProdutos += 1
    precoNovo = preco * 1.2
    print(f"Código do produto = {codigo} - Preço atualizado = {precoNovo}")
    codigo = int(input("Digite um código de produto: "))

if qtdeProdutos > 0:
    media = somaPrecos / qtdeProdutos
    print(f"Média dos preços sem aumento = {media}")
    print(f"Média dos preços com aumento = {media * 1.2}")