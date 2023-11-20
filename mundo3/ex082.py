# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    rep = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if rep == 'N':
        break
    else:
        while rep != 'S':
            print('Opção inválida! Tente novamente.')
            rep = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
