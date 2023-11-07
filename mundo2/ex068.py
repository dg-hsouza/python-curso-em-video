# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

cont = 0
soma = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)

while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        print('Escolha inválida. Tente novamente.')
        escolha = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    soma = computador + jogador
    sleep(0.5)
    print('PAR OU IMPAR...')
    sleep(1)
    print(f'Jogador jogou {jogador} e o computador jogou {computador}, a soma entre eles é {soma}')
    if soma % 2 == 0:
        resultado = 'P'
    elif soma % 2 == 1:
        resultado = 'I'
    sleep(1)
    if escolha == resultado:
        print('Parabéns! Você venceu.')
        cont = cont + 1
    else:
        break
print(f'Você conseguiu vencer {cont} vezes!')
