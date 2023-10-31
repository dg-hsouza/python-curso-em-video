# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade: até 9 anos: mirim / até 14 anos: infantil / até 19 anos: júnior
# até 25 anos: sênior / acima: master

from datetime import date

nome = str(input('Nome do atleta: '))
anoNasc = int(input('Ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNasc

print('O atleta {} tem {} anos'.format(nome, idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

