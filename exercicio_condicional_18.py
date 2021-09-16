# Escreva um programa que receba dois números reais e um código de seleção do usuário.
# Se o código digitado for 1, faça o programa adicionar os dois números previamente digitados e mostrar o resultado;
# se o código de seleção for 2, os números devem ser multiplicados;
# se o código de seleção for 3, o primeiro número deve ser dividido pelo segundo.
# Se nenhuma das opções acima for escolhida, mostrar "Código inválido".

codigo = int(input("Digite o código de seleção: "))

if codigo < 1 or codigo > 3:
    print("Código inválido")
else:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número:  "))
    if codigo == 1:
        print(f"Soma = {numero1 + numero2}")
    else:
        if codigo == 2:
            print(f"Multiplicação = {numero1 * numero2}")
        else:
            if numero2 == 0:
                print("Não pode ter divisão por zero")
            else:
                print(f"Divisão = {numero1 / numero2}")


