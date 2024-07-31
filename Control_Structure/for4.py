'''
funcao sortear dado 6 numeros entre 1 a 6
for com range 1 a 6
se for impar, continue
se for par e se for igual ao valor sorteado pela funcao dado, imprimir 'ACERTOU' e depois chamar o break
'''

from random import randint

def draw_dice():
    return randint(1, 6)


if __name__ == '__main__':
    for x in range(1, 7):
        if x % 2 != 0:
            continue

        if x == draw_dice(): #one chance?
            print('ACERTOU', x)
            break
    else: 
        print('ERROU')

#utilizar o else em um for, significa interagir o laco for por inteiro ate encontrar um "break", se nao encontrar, o else e executado