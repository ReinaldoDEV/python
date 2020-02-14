var = int(input('Selecione a quantidade de termos da sequencia de Fibonacci: '))
print('=='*20)

t1 = 0
t2 = 1
print('{} => {}'.format(t1, t2), end='')

for x in range(var):
    t3 = t1 + t2
    print(' => {}'.format(t3), end='')
    t1 = t2
    t2 = t3

print(' => FIM!')