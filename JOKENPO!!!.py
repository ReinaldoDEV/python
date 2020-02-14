#JO KEN PO!!!

from random import randint
from time import sleep


cpu = randint(0, 2)
var = ['Pedra', 'Papel', 'Tesoura']
print('=='*15)
print('''    [0] Pedra
    [1] Papel
    [2] Tesoura''')

player = int(input('Qual você escolhe?'))
print('=='*15)

string = ['JO', 'KEN', 'PO']
for v in string: #Timing para JOKENPO
    print(v)
    sleep(1)

if cpu == 0: #Caso cpu escolha PEDRA
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('Jogador GANHOU!')
    elif player == 2:
        print('Jogador PERDEU!')

elif cpu == 1: #Caso cpu escolha PAPEL
    if player == 0:
        print('Jogador PERDEU!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('Jogador GANHOU!')

elif cpu == 2: #Caso cpu escolha TESOURA
    if player == 0:
        print('Jogador GANHOU!')
    elif player == 1:
        print('Jogador PERDEU!')
    elif player == 2:
        print('EMPATE!')
print(cpu)





