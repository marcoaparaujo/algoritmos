dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
data = int(str(mes) + str(dia))
if data <= 321 or data > 1221:
    print("Verao")
else:
    if data <= 621:
        print("Outono")
    else:
        if data <= 923:
            print("Inverno")
        else:
            print ("Primavera")