# Uma encomenda de unidades de disco contém unidades marcadas com um código de 1 a 4,
# que indica o tipo seguinte:
# Código 	Tipo da unidade
# 1   	    CD-ROM (700MB)
# 2   	    DVD-ROM (4.7GB)
# 3   	    DVD-9 (8.54 GB)
# 4   	    Blu-Ray (25 GB)
# Escreva um programa que receba o número de um código como entrada e, baseado no valor digitado,
# informe o tipo correto de unidade de disco.

codigo = int(input("Digite o código da unidade de disco: "))
if codigo < 1 or codigo > 4:
    resultado = "Código inválido"
else:
    if codigo == 1:
        resultado = "CD-ROM (700MB)"
    else:
        if codigo == 2:
            resultado = "DVD-ROM (4.7GB)"
        else:
            if codigo == 3:
                resultado = "DVD-9 (8.54 GB)"
            else:
                resultado = "Blu-Ray (25 GB)"
                
print(resultado)