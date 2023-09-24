# Texto adaptavel

def adaptavel(text):
    print(f'~' * (len(text)+4))
    print(' ', text)
    print(f'~' * (len(text) + 4))


texto = str(input('Digite sua frase: '))
adaptavel(texto)
adaptavel('Esse eu fiz na mão')
