# Faça uma função que recebe, por parâmetro, uma matriz 6x6 e
# retorna o menor elemento da sua diagonal secundária.

def menor_diagonal_secundaria(matriz):
        menor = matriz[0][len(matriz)-1]
        for i in range(len(matriz)):
                if matriz[i][len(matriz) - 1 - i] < menor:
                        menor = matriz[i][len(matriz) - 1 - i]
        return menor

matriz = [[1, 2, 3, 4, 5, 6],
          [2, 3, 4, 5, 2, 2],
          [3, 4, 5, 4, 7, 3],
          [4, 5, 1, 7, 8, 4],
          [4, 2, 6, 7, 8, 5],
          [0, 6, 7, 8, 9, 7]]

print(f"Menor elemento diagonal secundária = {menor_diagonal_secundaria(matriz)}")
