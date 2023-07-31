#pedra papel tesouraa
import random
aposta = int(input('Escolha um: \n'
               '1 - Pedra \n'
               '2 - Papel \n'
               '3 - Tesoura \n'))

aposta2 = random.randint(1, 3)
print('-=' * 10)
if aposta == aposta2:
    print('EMPATE')
elif aposta == 1 and aposta2 == 2:
    print('PC jogou: Papel')
    print('Você jogou: Pedra')
    print('PERDEU!')
elif aposta == 1 & aposta2 == 3:
    print('PC jogou: Tesoura')
    print('Você jogou: Pedra')
    print('GANHOU!')
elif aposta == 2 and aposta2 == 1:
    print('PC jogou: Pedra')
    print('Você jogou: Papel')
    print('GANHOU!')
elif aposta == 2 and aposta2 == 3:
    print('PC jogou: Tesoura')
    print('Você jogou: Papel')
    print('PERDEU!')
elif aposta == 3 and aposta2 == 2:
    print('PC jogou: Papel')
    print('Você jogou: Tesoura')
    print('GANHOU!')
elif aposta == 3 and aposta2 == 1:
    print('PC jogou: Pedra')
    print('Você jogou: Tesoura')
    print('PERDEU!')
else:
    print('Digite corretamente.')

print('-=' * 10)