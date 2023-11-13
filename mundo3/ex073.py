# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre: A) apenas os 5 primeiros colocados. B) os últimos 4 colocados da tabela.
# C) uma lista com os times em ordem alfabética. D) em que posição está o time do Santos.

times = ('Botafogo', 'Grêmio', 'Palmeiras', 'RB Bragantino', 'Flamengo', 'Atlético MG', 'Athletico PR', 'Fluminense', 
         'São Paulo', 'Cuiabá', 'Fortaleza', 'Internacional', 'Santos', 'Corinthians', 'Bahia', 'Vasco', 'Cruzeiro', 
         'Goiás', 'Coritiba', 'América MG')

print('Os primeiros 5 colocados são: ')
for c in range(1, 6):
    print(f'{c}º {times[c - 1]}')
print('-=-' * 15)

print('Os últimos 4 colocados da tabela são: ')
for c in range(17, 21):
    print(f'{c}º {times[c - 1]}')
print('-=-' * 15)

print('Os times em ordem alfabética: ')
for c in range(1, 21):
    print(f'{c}º {sorted(times)[c - 1]}')
print('-=-' * 15)

print('O time Santos está na posição', times.index('Santos') + 1)
