# Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado
# o cargo correspondente. Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem
# de código inválido. Utilize a tabela abaixo:
# Código 	Cargo
# 101   	Vendedor
# 102   	Atendente
# 103   	Auxiliar Técnico
# 104   	Assistente
# 105   	Coordenador de Grupo
# 106   	Gerente

codigo = int(input("Digite um código: "))

if codigo < 101 or codigo > 106:
    mensagem = "Código inválido"
else:
    if codigo == 101:
        mensagem = "Vendedor"
    else:
        if codigo == 102:
            mensagem = "Atendente"
        else:
            if codigo == 103:
                mensagem = "Auxiliar técnico"
            else:
                if codigo == 104:
                    mensagem = "Assistente"
                else:
                    if codigo == 105:
                        mensagem = "Coordenador de Grupo"
                    else:
                        mensagem = "Gerente"

print(mensagem)