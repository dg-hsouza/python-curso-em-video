# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

cont = 0

while True:
    print('-=' * 15)
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for c in range (1, 11):
        total = num * c
        print(f'{num} x {c} = {total}')
print('Fim... até breve!')
