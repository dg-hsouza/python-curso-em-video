# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

lista = {}

nome = str(input('Nome: '))
lista['Nome'] = nome
nasc = int(input('Ano de Nascimento: '))

atual = datetime.now().year
idade = atual - nasc

lista['Idade'] = idade

ctps = int(input('Carteira de Trabalho (0 não tem): '))
lista['CTPS'] = ctps
if ctps == 0:
    print()
else:
    ano = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$'))
    apos = (ano + 35) - nasc
    lista['Contratação'] = ano
    lista['Salário'] = sal
    lista['Aposentadoria'] = apos

atual = datetime.now().year
idade = atual - nasc

print('-=' * 30)

for k, v in lista.items():
    print(f'{k} tem o valor {v}')
