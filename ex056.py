#analisador

media = 0
idmaior = 0
nomemaior = 0
qtdmulhermenosvinte = 0
for c in range(1, 4):
    print('---- {}ª Pessoa ----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper())
    media = media + idade
    if idmaior < idade and sexo == 'M':
        idmaior = idade
        nomemaior = nome
    if sexo == 'F' and idade < 20:
        qtdmulhermenosvinte += 1

media = float(media/3)

print('-'*8)
print('A média de idades é {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomemaior, idmaior))
print('A quantidade de Mulheres com menos de 20 anos é {}'.format(qtdmulhermenosvinte))
print('-'*8)
