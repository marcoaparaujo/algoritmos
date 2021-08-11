from datetime import date
from datetime import datetime

print("\nData atual")
data_atual = date.today()
print(data_atual)

print("\nSeparando os elementos de uma data")
print (data_atual.day)
print (data_atual.month)
print (data_atual.year)

print("\nConverter data em texto")
data_texto = data_atual.strftime("%d/%m/%Y")
print(data_texto)

print("\nConverter texto em data")
d1 = datetime.strptime('01/12/2020', '%d/%m/%Y')
d2 = datetime.strptime('2020-12-04', '%Y-%m-%d')
print(d1)
print(d2)

print("\nCalcular diferença de dias entre datas")
quantidade_dias = (d2 - d1).days
print(quantidade_dias)

print("\nComo incrementar dias em uma data")
print (date.fromordinal(data_atual.toordinal()+45))

print("\nDia da semana de uma data - seg=0, dom=6")
print(data_atual.weekday())

print("\nNome dia da semana")
dia_semana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
print (dia_semana[data_atual.weekday()])

