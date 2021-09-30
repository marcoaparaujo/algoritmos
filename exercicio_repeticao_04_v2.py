# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# O final da leitura de dados se dará com a entrada de um salário negativo.

somaSalarios = 0
somaFilhos = 0
maiorSalario = 0
qtdePessoasSalario1000 = 0

habitantes = 0

salario = float(input(f"Digite o salário do habitante {habitantes + 1}: "))
while salario >= 0:
    filhos = -1
    while filhos < 0:
        filhos = int(input(f"Digite o número de filhos do habitante {habitantes + 1}: "))
    somaSalarios += salario
    somaFilhos += filhos
    if salario > maiorSalario:
        maiorSalario = salario
    if salario <= 1000:
        qtdePessoasSalario1000 += 1
    habitantes += 1
    salario = float(input(f"Digite o salário do habitante {habitantes + 1}: "))

if habitantes > 0:
    print(f"Média dos salários = {somaSalarios / habitantes:.2f}")
    print(f"Média de filhos = {somaFilhos / habitantes:.2f}")
    print(f"Maior salário = {maiorSalario:.2f}")
    print(f"Percentual de pessoas que ganham até R$ 1.000 = {(qtdePessoasSalario1000 / habitantes) * 100:.2f}%")



