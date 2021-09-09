# Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))

# if numero1 < numero2 and numero1 < numero3 and numero1 < numero4:
#     print(f"O primeiro número é o menor com o valor {numero1}")
# else:
#     if numero2 < numero1 and numero2 < numero3 and numero2 < numero4:
#         print(f"O segundo número é o menor com o valor {numero2}")
#     else:
#         if numero3 < numero1 and numero3 < numero2 and numero3 < numero4:
#             print(f"O terceiro número é o menor com o valor {numero3}")
#         else:
#             print(f"O quarto número é o menor com o valor {numero4}")

menor = numero1

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
if numero4 < menor:
    menor = numero4

print(f"O menor número é o {menor}")


