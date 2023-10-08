# Votos
# não funciona, mas eu tivnha certeza absoluta que tava certo
from datetime import date

def voto(idade):
    if idade < 16:
        return 'Negado!'
    elif idade > 18:
       return 'Obrigatório!'
    else:
       return 'Opcional!'


ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano
print(f'Com {idade} o voto é: {voto(ano)}')

