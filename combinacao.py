palavra = 'ARARA'

posicao = []
resultado = []
resposta = []

for i in range(len(palavra)):
    posicao.append(0)

for i in range(len(palavra) ** len(palavra)):

    valido = True
    for k in range(len(palavra)):
        if posicao.count(k) != 1:
            valido = False
    if valido:
        resultado.append(posicao.copy())

    parar = False
    j = len(palavra) - 1
    while j >= 0 and not parar:
        posicao[j] = posicao[j] + 1

        if posicao[j] < len(palavra):
            parar = True;
        else:
            posicao[j] = 0
            j = j - 1


for i in range(len(resultado)):

    nova_palavra = ''
    for j in range(len(palavra)):
        nova_palavra = nova_palavra + palavra[resultado[i][j]]

    if nova_palavra not in resposta:
        resposta.append(nova_palavra)

print(len(resposta))
print(resposta)