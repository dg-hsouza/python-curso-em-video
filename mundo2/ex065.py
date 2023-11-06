# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

num = 0
cont = 0
soma = 0
maior = 0
menor = 0
seguir = 'S'

while seguir in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    seguir = str(input('Deseja inserir outro valor? [S/N] ')).upper().strip()[0]
print('Foram digitados {} números'.format(cont))

media = soma / cont
print('A média dos números digitados foi {}'.format(media))

print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
