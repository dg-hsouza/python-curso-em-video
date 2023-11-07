# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.

sexo = ''
cont = 0
conth = 0
contm = 0

while True:
    idade = int(input('Qual é a sua idade: '))
    if idade >= 18:
        cont = cont + 1
    sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]
    if sexo not in 'MmFf':
        print('Sexo inválido. Tente novamente.')
        while sexo not in 'MmFf':
            sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        conth = conth + 1
    if sexo == 'F' and idade < 20:
        contm = contm + 1
    print('Cadastro realizado com sucesso!')
    print('=' * 35)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'SsNn':
        print('Opção inválida. Tente novamente.')
        while continuar not in 'SsNn':
            continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    print('=' * 35)
print('Fim...')

print(f'{cont} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {conth} homens.')
print(f'{contm} mulheres tem menos de 20 anos.')
