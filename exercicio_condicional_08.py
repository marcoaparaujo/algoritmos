# Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade.
# A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 10 anos), adolescente (11 a 18 anos),
# adulta (19 a 50 anos) ou idosa (51 anos em diante).

anoAtual = int(input("Digite o ano atual: "))
anoNascimento = int(input("Digite o ano de nascimento: "))
idade = anoAtual - anoNascimento

if idade < 0:
    print("Idade inválida")
else:
    if idade <= 3:
        print("Bebê")
    else:
        if idade <= 10:
            print("Criança")
        else:
            if idade <= 18:
                print("Adolescente")
            else:
                if idade <= 50:
                    print("Adulto")
                else:
                    print("Idoso")
