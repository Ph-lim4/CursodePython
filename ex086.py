# Matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número [{l}, {c}]: '))
print('-' * 40)
for l1 in range(0, 3):
    for c1 in range(0, 3):
        print(f'|{matriz[l1][c1]:^5}|', end='')
    print()
