num = int(input('Digite um número: '))
div = 0

for var in range(1, num+1):
    if num % var == 0: # Se for divisivel
        print('\033[32m', end='')
        div += 1
    else:
        print('\033[m', end='')
    print(f'{var} ', end='')

print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, div))

if div == 2:
    print('É um número \033[32mPRIMO!!!')
else:
    print('\033[31mNÃO \033[mé um número \033[32mPRIMO')