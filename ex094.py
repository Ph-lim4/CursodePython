# Unindo Dicionario e Listas
pessoas = list()
individuo = dict()
soma = media = woman = 0
while True:
    individuo.clear()
    individuo['nome'] = str(input('Nome: '))
    while True:
        individuo['sexo'] = str(input('Sexo (M/F): '))
        if individuo['sexo'] in 'MmFf':
            break
        print('ERRO, apenas digite F ou M')
    individuo['idade'] = float(input('Idade: '))
    soma += individuo['idade']
    pessoas.append(individuo.copy())
    while True:
        resp = str(input('Quer continuar (S/N): '))
        if resp in 'SsNn':
            break
        print('ERRO, apenas digite S ou N')
    if resp in 'Nn':
        break
print('=-'*20)
print(f'A) Ao todo temos {len(pessoas)} Pessoas cadastradas')
media = soma / len(pessoas)
print(f'B) A média de idade é {media}')
print(f'C) As mulheres cadastradas são: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()
print('<<<<ENCERRADO>>>>')

