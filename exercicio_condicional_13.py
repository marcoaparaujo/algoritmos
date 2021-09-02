# Baseado no ano e peso do modelo de um automóvel, o estado de Nova Jersey determina a sua classe de peso e
# taxa de registro usando a seguinte tabela:
#
# Ano do modelo	    Peso	        Classe	Taxa de registro
# 1970 ou antes 	Menos de 1200 kg	1	16,50
# 	                de 1200 a 1700 kg	2	25,50
# 	                Mais de 1700 kg	    3	46,50
# 1971 a 1979	    Menos de 1200 kg	4	27,00
# 	                de 1200 a 1700 kg	5	30,50
# 	                Mais de 1700 kg	    6	52,50
# 1980 ou depois 	Menos de 1600 kg	7	19,50
# 	                1600 kg ou mais	    8	55,50
#
# Usando esta informação, escreva um programa que receba o ano e o peso do modelo de um automóvel e
# calcule e imprima a classe de peso e a taxa de registro para o carro.

ano = int(input("Digite o ano: "))
peso = int(input("Digite o peso: "))

if ano <= 1970:
    if peso < 1200:
        classe = 1
        taxa = 16.50
    else:
        if peso <= 1700:
            classe = 2
            taxa = 25.5
        else:
            classe = 3
            taxa = 46.50
else:
    if ano <= 1979:
        if peso < 1200:
            classe = 4
            taxa = 27.0
        else:
            if peso <= 1700:
                classe = 5
                taxa = 30.50
            else:
                classe = 6
                taxa = 52.50
    else:
        if peso < 1600:
            classe = 7
            taxa = 19.5
        else:
            classe = 8
            taxa = 55.5

print(f"Classe = {classe}")
print(f"Taxa = {taxa:.2f}")


