# Melhore o EX061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

print('=' * 30)
print('{:^30}'.format(' 10 TERMOS DE UMA PA '))
print('=' * 30)

prime = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = prime
conta = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while conta <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        conta = conta + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
