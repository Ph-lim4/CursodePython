#validador de dados

sexo = str(input("Sexo: ")).strip().upper()[0]

while sexo not in 'MnFf':
    sexo = str(input('Dados invalidos, digite novamente: ')).strip().upper()[0]
print('Sexo {}'.format(sexo))