# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Digite seu nome: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    situacao = 'Aprovado'
elif 6 <= media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

dicionario = {'Nome': nome, 'Média': media, 'Situação': situacao}

for k, v in dicionario.items():
    print(f'{k} é igual a {v}')
