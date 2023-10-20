# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um número qualquer: '))

calc = num % 2

if calc == 0:
    print('O número {} é PAR'.format(num))
elif calc == 1:
    print('O número {} é ÍMPAR'.format(num))
