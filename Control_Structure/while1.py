#lib de valores random
from random import randint

number = -1
secret = randint(0, 9)

#ambos serao alterados na execucao do codigo
while number != secret:
    number = int(input('Insira o numero: '))

print(f'O numero secreto e: {secret}')


