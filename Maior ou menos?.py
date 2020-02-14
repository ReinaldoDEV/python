#Mostre o numero maior e menos de uma lista de 5 numeros

maior = menor = 0

for var in range(1, 6):
    num = int(input(f'Digite o {var}º numero: '))
    if var == 1: # Na primeira leitura ambos recebem o mesmo valor
        meior = num
        menor = num
    else: # Se para de acordo com o valor
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print(f'O maior numero foi {maior} e o menor foi {menor}')
