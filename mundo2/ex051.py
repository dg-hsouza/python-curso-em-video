# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No, final, mostre os 10 primeiros
# termos dessa progressão.

print('=' * 30)
print('{:^30}'.format(' 10 TERMOS DE UMA PA '))
print('=' * 30)

prime = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = prime + (10 - 1) * razao

for c in range(prime, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')
