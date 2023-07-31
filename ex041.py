#atletas
import datetime

ano = int(input('ANO: '))
idade = datetime.date.today().year - ano

print('Tem {} anos'.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')

