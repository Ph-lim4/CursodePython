# Nota do Aluno, média e Situação
aluno = dict()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input(f"Media de {aluno['nome']}: "))
print('-'*20)
print(f'O nome é {aluno["nome"]}.')
print(f'A média: {aluno["media"]}')
if aluno['media'] < 7:
    print(f'{aluno["nome"]} está de Recuperação!')
else:
    print(f'{aluno["nome"]} Passou!')


# Outra forma seria:
# - Utilizar um campo no dicionario chamado "Situação", que teria:
#       - Aprovado, Recuperação e Reprovado(>7,5>7,<5)
# para exibir:
#   for k, v in aluno.items():
#   print(f' - {k} é igual a {v}')
#   ex:
#   print(f' - {'situação'} é igual a {'Aprovado'}')
