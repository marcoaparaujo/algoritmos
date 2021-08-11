# Faça uma função recursiva que calcule o fatorial de um número.

def fatorial(n):
    if n == 1:
        return 1

    return n * fatorial(n - 1)

print(fatorial(4))