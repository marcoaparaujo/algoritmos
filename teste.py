valores = []
maior = 0
for contador in range(10):
    valores.append(int(input(f"Digite o {contador + 1}o. valor: ")))
    if valores[contador] > maior:
        maior = valores[contador]
quantidade = 0
for contador in range(10):
    if valores[contador] == maior:
        quantidade = quantidade + 1
print(f"O maior valor {maior} aparece {quantidade} de vezes no vetor {valores}")
