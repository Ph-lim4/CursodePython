# Funções
def lin():
    print('-'*20)


def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)


def soma(a, b):
    s = a + b
    print(s)


def contador(* num):
    for valor in num:
        print(valor)


def dobralist(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lin()
print('Teste')
lin()
mensagem('Testando...')
soma(2, 7)
contador(1, 2, 3, 8)
valores = [2, 4, 6]
dobralist(valores)
print(valores)

