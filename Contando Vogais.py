#Faça um programa que leia as falavras do usuario e add em uma lista. Depois mostre as jogais de cada palavra

lista = []
print('Digite apenas uma palavra e utilize a palavra "exit" para finalizar')
while True:
    var = str(input('Digite sua plavra:').upper())

    if var == 'EXIT':
        break
    else:
        lista.append(var)

for p in lista: #Analisa as palavras
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p: #Analisa as letras
        if letra.lower() in 'aeiou':
            print(letra, end='')
