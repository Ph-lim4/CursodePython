# contagem regressiva
from time import sleep
num = int(input())
for cont in range(num, 0, -1):
    print(cont)
    sleep(1)

print('POW!')