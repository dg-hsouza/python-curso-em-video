# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto():
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        vt = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        vt = 'VOTO OPCIONAL'
    else:
        vt = 'VOTO OBRIGATÓRIO'
    print(f'Com {idade} anos: {vt}.')

print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
voto()
