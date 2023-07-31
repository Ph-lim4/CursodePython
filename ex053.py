#palindromo

frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
print(junto)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto :
    print('É um Palindromo!!!')
else:
    print('Não é um palindromo...')




