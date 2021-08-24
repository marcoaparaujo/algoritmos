# Ler um número inteiro e testar se o valor lido termina com 0 (divisível por 10).
# Em caso positivo, exiba a metade deste número. Caso contrário, exibir a mensagem
# "O número digitado não termina com 0".

numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print(numero/2)
else:
    print("O número digitado não termina com 0")
