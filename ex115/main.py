from ex115.menu import *
from ex115.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criararquivo(arq)

while True:
    resposta = menu()
    if resposta == 1:
        # READ - Leitura do Arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # CREAT - Cria um novo registro no Arquivo
        cabeçalho('NOVO REGISTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    else:
        cabeçalho('Saindo do sistema, até logo!')
        break
