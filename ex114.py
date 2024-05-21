#esse eu não consegui, todas as libs que tentei deram erro

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print('Não está acessivel')
else:
    print('Está acessivel')