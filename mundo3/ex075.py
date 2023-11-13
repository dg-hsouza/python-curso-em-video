# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) quantas vezes apareceu o valor 9. B) em que posição foi digitado o primeiro valor 3.
# C) quais foram os números pares.

num = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), int(input('Digite o 3º número: ')), 
       int(input('Digite o 4º número: ')))

print(f'Você digitou os valores {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posição {num.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado.')

print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
