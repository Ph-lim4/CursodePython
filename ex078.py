# Maior e menor na posição x

num = [
int(input('Digite um valor para a posição 0: ')),
int(input('Digite um valor para a posição 1: ')),
int(input('Digite um valor para a posição 2: ')),
int(input('Digite um valor para a posição 3: ')),
int(input('Digite um valor para a posição 4: ')),
]
maior = max(num)
menor = min(num)

print(num)
print(f'O maior número foi {max(num)} nas posições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número foi {min(num)} nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()