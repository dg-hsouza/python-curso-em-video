# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

lista = {}

print('Valores sorteados:')
for joga in range(1, 5):
    dado = randint(1,6)
    print(f'    O jogador{joga} tirou {dado}')
    lista[f'Jogador{joga}'] = dado
    sleep(1)

sleep(1)

print('Ranking dos jogadores:')
cont = 1

ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
for k, v in ranking:
    print(f'    {cont}º lugar: {k} com {v}')
    cont = cont + 1
    sleep(1)
