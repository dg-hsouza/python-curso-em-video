# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

num = float(input('Digite um valor: '))
part = int(num)

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, part))
