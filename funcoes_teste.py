def exibirTitulo(mensagem, qtde):
    for i in range(0, qtde):
        print(mensagem)

def somar(valor1, valor2):
     return valor1 + valor2

def subtrair(valor1, valor2):
     return valor1 - valor2

def multiplicar(valor1, valor2):
    return valor1 * valor2

def dividir(valor1, valor2):
    if valor2 == 0:
        return 0
    else:
        return valor1 / valor2


exibirTitulo("Calculadora", 1)
exibirTitulo("-----------", 1)
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação: ")

if operacao == "+":
    resposta = somar(numero1, numero2)
else:
    if operacao == "-":
        resposta = subtrair(numero1, numero2)
    else:
        if operacao == "*":
            resposta = multiplicar(numero1, numero2)
        else:
            if operacao == "/":
                resposta = dividir(numero1, numero2)

print(resposta)