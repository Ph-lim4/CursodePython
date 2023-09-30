# Maior com função

def maior(* num):
    cont = maior = 0
    print('Analisando dados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if valor > maior:
            maior = valor
    print()
    print(f'O maior é: {maior}')
    print('-' * 30)


maior(1, 2, 3, 4, 5)
maior(20, 10, 15, 5)
