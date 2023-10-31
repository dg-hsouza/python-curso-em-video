# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento: -à vista dinheiro/ cheque: 10% de desconto // -à vista no cartão: 5% de desconto
# -em até 2x no cartão: preço normal // -3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS AMERICANAS '))
preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é a opção? '))

desconto10 = preco - (preco / 100 * 10)
desconto5 = preco - (preco / 100 * 5)

parcela = 2
parcela2 = preco / parcela
total2 = parcela2 * parcela

juros = preco + (preco / 100 * 20)

if opc == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desconto10))
elif opc == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desconto5))
elif opc == 3:
    print('Sua compra vai ser parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total2))
elif opc == 4:
    parcelas = int(input('Quantas parcelas? '))
    parcela3 = juros / parcelas
    total3 = parcela3 * parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, parcela3))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total3))
else:
    print('Opção inválida. Tente novamente.')

