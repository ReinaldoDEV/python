

saldo = float(input('Qual o valor total das compras: R$'))

print('''QUAL A FORMA DE PAGAMENTO?
    [1] A vista (DINHEIRO/DEBITO)
    [2] A vista (CARTÃO DE CRÉDITO)
    [3] 2x No crédito
    [4] 3x No crédito''')

opc = int(input('Qual é a opção? '))
print('=='*20)

if opc == 1:
    total = saldo - (saldo * 10 / 100) # 10% off no pagamento
    print('Sua compra no valor de R${:.2f} ficar com 10% de desconto e vai custar R${:.2f}'.format(saldo, total))
elif opc == 2:
    total = saldo - (saldo * 5 / 100) # 5% off no pagamento
    print('Sua compra no valor de R${:.2f} ficar com 5% de desconto e vai custar R${:.2f}'.format(saldo, total))
elif opc == 3:
    total = saldo # Preço normal do produto
    parcela = saldo / 2
    print('Sua compra no valor de R${:.2f} será parcelada em 2x de {:.2f}'.format(saldo, parcela))
elif opc == 4:
    total = saldo + (saldo * 30/100) #Juros de 30%
    parcela = saldo / 3
    print('Sua compra no valor de R${:.2f} será parcelada em 2x de {:.2f} com 30% de juros'.format(saldo, parcela))