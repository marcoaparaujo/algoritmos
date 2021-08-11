somaSalario = 0
somaFilhos = 0
qtde = 0
menorCem = 0
salario = float(input("Digite o salario: "))
maiorSalario = salario
while salario >= 0:
    filhos = int(input("Digite o numero de filhos: "))
    somaSalario = somaSalario + salario
    somaFilhos = somaFilhos + filhos
    if salario > maiorSalario:
        maiorSalario = salario
    if salario < 100:
        menorCem = menorCem + 1
    qtde = qtde + 1

    salario = float(input("Digite o salario: "))
if qtde > 0:
    print (f"Media Salarios = {somaSalario/qtde}")
    print (f"Media Filhos = {somaFilhos/qtde}")
    print(f"Maior salario = {maiorSalario}")
    print (f"Percentual de pessoas com salario menor que 100 reais: {(menorCem/qtde)*100}%")
