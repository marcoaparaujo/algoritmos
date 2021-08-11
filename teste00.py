soma = 0
contador = 0
resposta = "S"

while resposta == "S" or resposta == "s":
    nota = float(input(f"Digite a nota do aluno {contador + 1}: "))
    if nota >= 0 and nota <= 10:
        soma = soma + nota
        contador = contador + 1
    resposta = ""
    while resposta != "S" and resposta != "s" and resposta != "N" and resposta != "n":
        resposta = input("Deseja continuar (S/N)? ")

if contador > 0:
    print(f"Media = {soma / contador}")


