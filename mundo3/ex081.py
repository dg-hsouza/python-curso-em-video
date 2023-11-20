# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) quantos números foram digitados. B) a lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont = cont + 1
    rep = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if rep == 'N':
        break
    else:
        while rep != 'S':
            print('Opção inválida! Tente novamente.')
            rep = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('-=' * 30)
print(f'Foram digitados {cont} números.')
print('Os valores em ordem decrescente são ', end='')
print(sorted(lista, reverse=True))
if 5 not in lista:
    print('O número 5 não foi digitado!')
else:
    print('O número 5 está na lista!')
