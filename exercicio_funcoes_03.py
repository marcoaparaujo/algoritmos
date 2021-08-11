# 3.	Faça uma função que recebe por parâmetro o raio de uma esfera e calcule o
# seu volume (v = (4 x pi x R**3)/3).  


def calcular_volume(r):
    return (4 * 3.1416 * r ** 3) / 3


raio = float(input("Digite o raio da esfera: "))
print(f"Volume = {calcular_volume(raio):.2f}")