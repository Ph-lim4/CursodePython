# Notas de alunos
cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'lilas:':'\033[35m',
    'azulc':'\033[36m',

    'bordabranca':'\033[1:30:40m',
    'bordavermelha': '\033[1:30:41m',
    'bordaverde': '\033[1:30:42m',
    'bordaamarela': '\033[1:30:43m',
    'bordaazul': '\033[1:30:44m',
    'bordalilas': '\033[1:30:45m',
    'bordaazulc': '\033[1:30:46m',
    'pretoebranco':'\033[7;30m',

}
alunonotas = []
print(f"{cores['bordaverde']}  Resgistrador de Notas  {cores['limpa']}")
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2)/2
    alunonotas.append([nome, nota1, nota2, media])
    resp = input('Quer continuar? (S/N): ')
    if resp in 'nN':
        break
print(f"{cores['bordaverde']} ---  Resultados  --- {cores['limpa']}")
print(f'{"Num.":<6}{"NOME":<10}{"MEDIA":<8}')
print('------------------------')
for c in range(0, len(alunonotas)):
    print(f'{c:<6}{alunonotas[c][0]:<10}{alunonotas[c][3]:<8.1f}')
print('------------------------')
while True:
    resp = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if resp == 999:
        break
    else:
        print(f'Notas de {alunonotas[resp][0]} são {alunonotas[resp][1]} e {alunonotas[resp][2]}')
        print('-' * 45)
