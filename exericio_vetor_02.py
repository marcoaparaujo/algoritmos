nome = input("Digite um nome: ")
letra = input("Digite uma letra a ser testada: ")

nome = nome.lower()

print(nome)

print(len(nome))

for i in range(len(nome)):
    print(nome[i])

print(letra in nome)

print(nome.count('A'))