#Tente acertar o numero que a maquina esta pensando...

from random import randint
from time import sleep

res = 'Y'

print('=='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

while True:
    maquina = randint(0, 5)
    print('=='*25)

    jogador = input('Em qual número eu pensei? ')
    print('Processando!!!')
    sleep(3)

    if jogador == maquina:
        print('PARABENS VOCE ACERTOU!!!')
    else:
        print('MEUS PARABENS! você ERROU! Eu pensei no numero {} e você escolheu {}' .format(maquina, jogador))

    res = input('Quer tentar novamente? Y/N: ').upper()
    if res == 'N':
        break
