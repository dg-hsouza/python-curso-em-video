# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Qual é a distância da sua viagem? '))
if dist > 0:
    print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dist))
else:
    print('Distância inválida')

if 0 < dist <= 200:
    preco = dist * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
elif dist > 200:
    preco = dist * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    print('Preço indisponível')
