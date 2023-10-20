# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math

catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))

hipot = math.sqrt(catop**2 + catad**2)

print('A hipotenusa vai medir {:.2f}'.format(hipot))
