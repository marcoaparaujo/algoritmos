valor_inteiro1 = int(input("Digite o primeiro número inteiro de 1 a 10: "))
valor_inteiro2 = int(input("Digite o segundo número inteiro de 1 a 10: "))
if valor_inteiro1 < 1 or valor_inteiro1 > 10 or valor_inteiro2 < 1 or valor_inteiro2 > 10:
    print("Valor inválido")
else:
    soma = valor_inteiro1 + valor_inteiro2
    if soma < 8:
        print(f"{soma/2:.2f}")
    else:
        if soma == 8:
            print(valor_inteiro1 * valor_inteiro2)
        else:
            if valor_inteiro1 > valor_inteiro2:
                print(f"{valor_inteiro1 / valor_inteiro2:.2f}")
            else:
                print(f"{valor_inteiro2 / valor_inteiro1:.2f}")

