# Refaça o EX051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('=' * 30)
print('{:^30}'.format(' 10 TERMOS DE UMA PA '))
print('=' * 30)

prime = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = prime
conta = 1

while conta <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    conta = conta + 1
print('ACABOU')
