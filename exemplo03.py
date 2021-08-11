# Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela "APROVADO",
# se for menor, imprimir reprovado.

nome = input("Digite seu nome: ")
nota = int(input("Digite uma nota: "))


if nota > 100:
    print("Nota inválida")
else:
    if nota < 0:
        print("Nota inválida")
    else:
        if nota >= 60:
            print(f"Parabéns!! {nome} você foi Aprovado")
            if nota >= 80:
                print("Foi bom demais!!")
        else:
            print(f"Infelizmente {nome} você foi Reprovado")
            if nota < 30:
                print("Vc precisa estudar mais")

print("Fim")
