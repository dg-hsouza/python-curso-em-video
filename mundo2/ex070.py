# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre: A) Qual é o total gasto na compra. B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

soma = 0
mil = 0
menor = 0
cont = 0
nome = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    soma = soma + preco
    cont = cont + 1
    if preco > 1000:
        mil = mil + 1
    if cont == 1:
        menor = preco
        nome = produto
    else:
        if preco < menor:
            menor = preco
            nome = produto
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'SsNn':
        print('Opção inválida. Tente novamente.')
        while continuar not in 'SsNn':
            continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Fim...')

print(f'Você comprou {cont} produtos')
print(f'O total gasto na compra foi de R${soma:.2f}')
print(f'{mil} produtos custaram mais de R$1000')
print(f'O produto mais barato foi {nome} e custou R${menor:.2f}')
