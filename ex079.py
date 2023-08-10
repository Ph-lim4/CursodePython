# Valores unicos em uma lista

listanum = []

while True:
    num = int(input('Digite um Número: '))
    if num in listanum:
        print('Valor já adicionado, tente novamente...')
    else:
        print('Valor Adicionado com sucesso!')
        listanum.append(num)
    resp = input('Quer continuar? (s/n): ').upper().strip()
    if resp == 'N':
        break
    else:
        print('-'*20)


listanum.sort()
print(f'Lista de numeros foi: {listanum}')
