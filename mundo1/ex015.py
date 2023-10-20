# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km.

dias = int(input('Quantos dias alugados? '))
dist = int(input('Quantos Km rodados? '))

diaria = 60 * dias
kmroda = 0.15 * dist
total = diaria + kmroda

print('O total a pagar é de R${:.2f}'.format(total))
