def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Digite um numero: "))
print(fibonacci(numero))