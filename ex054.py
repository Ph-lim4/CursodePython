#Maiores e menores
from datetime import date

nasc = 0
ano = date.today().year
idade = 0
maior = 0
menor = 0

for c in range(1, 4):
    nasc = int(input('Data de Nascimento da {}ª Pessoa: '.format(c)))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Maiores: {}'.format(maior))
print('Menores: {}'.format(menor))
