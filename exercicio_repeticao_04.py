# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$1000,00.
# Para isso, digitar no início a quantidade de habitantes

habitantes = int(input("Digite o número de habitantes: "))
if habitantes > 0:
    somaSalarios = 0
    somaFilhos = 0
    maiorSalario = 0
    qtdePessoasSalario1000 = 0

    for i in range(1, habitantes + 1):
        salario = float(input(f"Digite o salário do habitante {i}: "))
        filhos = int(input(f"Digite o número de filhos do habitante {i}: "))
        somaSalarios += salario
        somaFilhos += filhos
        if salario > maiorSalario:
            maiorSalario = salario
        if salario <= 1000:
            qtdePessoasSalario1000 += 1

    print(f"Média dos salários = {somaSalarios / habitantes:.2f}")
    print(f"Média de filhos = {somaFilhos / habitantes:.2f}")
    print(f"Maior salário = {maiorSalario:.2f}")
    print(f"Percentual de pessoas que ganham até R$ 1.000 = {(qtdePessoasSalario1000 / habitantes) * 100}%")



