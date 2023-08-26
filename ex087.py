# --------------------------------------------------
# ----------------Mais sobre matriz-----------------
# Se trata de um aprimoramento do exercicio anterior
# --------------------------------------------------

# Preenchendo a Matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número [{l}, {c}]: '))
print('-' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^5}|', end='')
    print()

# Tratando os dados
print('-'*45)
# Número de pares
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print(f'A soma dos valores pares é: {pares}')
# Soma dos valores da terceira coluna
terceiracoluna = 0
for l in range(0, 3):
    terceiracoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {terceiracoluna}')
# Maior valor da segunda linha
maior = 0
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
print('-'*45)
