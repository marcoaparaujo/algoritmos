# 2.	Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito,
# conforme a tabela abaixo: De 0 a 49 (D), De 50 a 69 (C), De 70 a 89 (B), De 90 a 100 (A)


def calcular_conceito(media):
    if media < 0 or media > 100:
        conceito = "Inválido"
    else:
        if media <= 49:
            conceito = "D"
        else:
            if media <= 69:
                conceito = "C"
            else:
                if media <= 89:
                    conceito = "B"
                else:
                    conceito = "A"
    return conceito


media_final = int(input("Digite sua média final: "))
print(f"Conceito {calcular_conceito(media_final)}")
