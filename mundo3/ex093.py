# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

lista = []
dicio = {}
soma = 0
cont = 0

dicio['nome'] = nome = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {nome} jogou? '))

for p in range(1, part + 1):
    gol = int(input(f'Quantos gols na partida {p}? '))
    lista.append(gol)
    soma = soma + gol
print('-=' * 30)

dicio['gols'] = lista
dicio['total'] = soma

for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {nome} jogou {part} partidas.')
for c in range(1, part + 1):
    print(f'   -> Na partida {c}, fez {lista[cont]} gols.')
    cont = cont + 1
print(f'Foi um total de {soma} gols.')
