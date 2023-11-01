# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
contme = 0
contma = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        contma = contma + 1
    elif idade < 21:
        contme = contme + 1

print('')
print('Ao todo tivemos {} pessoas maiores de idade'. format(contma))
print('E também tivemos {} pessoas menores de idade'.format(contme))
print('')
