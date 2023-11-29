# Aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

# jogador = []
# lista = []
# dicio = {}
# soma = 0
# cont = 0

# while True:
#     dicio['nome'] = nome = str(input('Nome do jogador: '))
#     part = int(input(f'Quantas partidas {nome} jogou? '))

#     for p in range(1, part + 1):
#         gol = int(input(f'Quantos gols na partida {p}? '))
#         lista.append(gol)
#         soma = soma + gol
#     jogador.append(dicio)
#     repete = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#     if repete == 'N':
#         break
#     else:
#         while repete != 'S':
#             print('Opção inválida. Tente novamente.')
#             repete = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#     print('-' * 30)
# print('-=' * 30)

# dicio['gols'] = lista
# dicio['total'] = soma

# print(f'O jogador {nome} jogou {part} partidas.')
# for c in range(1, part + 1):
#     print(f'   -> Na partida {c}, fez {lista[cont]} gols.')
#     cont = cont + 1
# print(f'Foi um total de {soma} gols.')

# print(jogador)






time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<<   VOLTE SEMPRE >>')
