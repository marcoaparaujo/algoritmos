# A taxa de juros aplicada em fundos depositados em um banco é determinada pelo
# tempo em que estes ficam depositados. Para um banco em particular, a seguinte tabela
# é usada:
# Tempo em depósito -> Taxa de juros
# Maior ou igual a 5 anos -> 0,95
# Menor que 5 anos mas maior ou igual a 4 anos -> 0,9
# Menor que 4 anos mas maior ou igual a 3 anos -> 0,85
# Menor que 3 anos mas maior ou igual a 2 anos -> 0,75
# Menor que 2 anos mas maior ou igual a 1 ano -> 0,65
# Menor que 1 ano -> 0,55
# Usando esta informação, escreva um programa que receba o tempo em que os fundos
# foram mantidos em depósito e informe a taxa de juros correspondente.

tempo_aplicacao = float(input("A quantos anos aplicação foi depositada? "))
if tempo_aplicacao >= 5:
    taxa_juros = 0.95
else:
     if tempo_aplicacao >= 4:
        taxa_juros = 0.9
     else:
          if tempo_aplicacao >= 3:
            taxa_juros = 0.85
          else:
                if tempo_aplicacao >= 2:
                    taxa_juros = 0.75
                else:
                    if tempo_aplicacao >= 1:
                        taxa_juros = 0.65
                    else:
                        taxa_juros = 0.55

print(f"O juros é de {taxa_juros}")




