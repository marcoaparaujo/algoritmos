# 4.	Escrever uma função contar_impar(n1, n2) que retorna o número de  inteiros ímpares
# que existem entre n1 e n2 (inclusive ambos, se for o caso).
# A  função deve funcionar inclusive se o valor de n2 for menor que n1.  


def contar_impar(n1, n2):
    if n2 < n1:
        aux = n1
        n1 = n2
        n2 = aux

    quantidade = 0;
    for num in range(n1, n2+1):
        if num % 2 == 1:
            quantidade = quantidade + 1
    return quantidade


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número : "))
resposta = contar_impar(num1, num2)
print(f"A quantidade de ímpares no intervalo = {resposta}")
