# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))

desconto = 5
novopreco = preco - (preco / 100 * desconto)

print('O produto que custava R${:.2f}, na promoção de {}% vai custar R${:.2f}'.format(preco, desconto, novopreco))
