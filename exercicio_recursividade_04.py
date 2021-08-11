# Pesquise a sequência de Fibonacci e faça uma função recursiva para exibir seus n primeiros termos,
# sendo n um parâmetro da função.

def fibonacci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

# 1 1 2 3 5 8 13 21 34


