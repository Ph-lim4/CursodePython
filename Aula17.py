# Anotações aula 17 : Listas
# Declaração
num = [1, 2, 3]
# Modificação
num[2] = 4
print(num)
# Acrecentando
num.append(7)
print(num)
# Ordenando
num.sort()
print(num)
num.sort(reverse=True)
print(num)
# inserir
num.insert(3, 5)
print(num)
# Removendo por posição
num.pop(3)
print(num)
# Tamanho
print(f'Tamanho atual {len(num)}')
# Removendo por valor
num.remove(2)
print(num)

# Aprensentando Valores
print('Apresentando Valores: ')
# Valor:
for n in num:
    print(n, end=' ')
print()
# index
print('------', num.index(4))
# Valor e posição
for p, n in enumerate(num):
    print(p, '-', n)

# Adicionando valores por meio do for
for cont in range(0, 5):
    num.append(int(input('Valor: ')))
print(f'Valor no final: {num}')

# Criando uma Cópia de NUM
num2 = num[:]
print(num2)