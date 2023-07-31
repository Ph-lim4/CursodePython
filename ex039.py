#alistamento Militar
import datetime

ano = int(input('Ano de nascimento: '))
anoatual = datetime.date.today().year
idade = int(anoatual - ano)

if (idade == 18):

    print('''Quem nasceu em {} tem {} anos em {}
    Seu alistamento é esse ano'''
          .format(ano, idade, anoatual))
elif (idade < 18):
    faltam = 18 - idade
    anoalis = anoatual + faltam
    print('''Quem nasceu em {} tem {} anos em {}
    Ainda faltam {} anos para seu alistamento,
    Será em {}'''
          .format(ano, idade, anoatual, faltam, anoalis))
else:
    sobram = idade - 18
    anoalis = anoatual - sobram
    print('''Quem nasceu em {} tem {} anos em {}
    Você deveria ter se alistado {} anos atrás,
    Seu alistamento foi em {}'''
          .format(ano, idade, anoatual, sobram, anoalis))
