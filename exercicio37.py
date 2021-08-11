# Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos,
# digitados pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.  

soma_valor = 0
qtde_valores = 0
valor = int(input("Digite um valor: "))
while valor >= 0:
    soma_valor = soma_valor + valor
    qtde_valores = qtde_valores + 1
    valor = int(input("Digite um valor: "))

if qtde_valores > 0:
    print(f"Média = {soma_valor / qtde_valores:.2f}")