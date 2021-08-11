def somar(valor1, valor2):
    return valor1 + valor2

def subtrair(valor1, valor2):
    return valor1 - valor2

def multiplicar(valor1, valor2):
    return valor1 * valor2

def dividir(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return 0


continuar = 'S'
while continuar == 'S' or continuar == 's':
    num1 = int(input("Digite um número   : "))
    num2 = int(input("Digite outro número: "))
    operacao = input("Digite a operacao  : ")

    if operacao == '+':
        resultado = somar(num1, num2)
    else:
        if operacao == '-':
            resultado = subtrair(num1, num2)
        else:
            if operacao == '*':
                resultado = multiplicar(num1, num2)
            else:
                if operacao == '/':
                    resultado = dividir(num1, num2)

    print(f"Resultado = {resultado:.2f}")

    continuar = input("Deseja continuar (S/N)? ")
