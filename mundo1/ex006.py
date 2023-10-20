# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math


num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

print('O dobro de {} vale {}.'.format(num, dobro))
print('O triplo de {} vale {}.'.format(num, triplo))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, raiz))
