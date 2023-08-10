# Contando vogais
palavras = ('Amor', 'da', 'Minha', 'Vida', 'Todinha')

for p in palavras:
    print(f'\nNa palavra {p} Temos:', end=' ')
    # Cada cadeia de caractere também é uma lista, sendo possivel utilizar o mesmo metodo
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
