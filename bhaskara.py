continua = ''
while continua != 'q':
    print('Calculando as raízes de uma equação de 2º grau\n')

    a = float(input('Digite um valor para A: '))
    b = float(input('Digite um valor para B: '))
    c = float(input('Digite um valor para C: '))

    delta = (b ** 2) - (4 * a * c)

    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f'\nValor de x1: {x1}')
    print(f'Valor de x2: {x2}')

    continua = input('\nDeseja sair? Digite q ou Enter para um novo cálculo: \n')
