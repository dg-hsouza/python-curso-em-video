# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

l1 = []
l2 = []
l3 = []

for c in range(0, 3):
    n1 = int(input(f'Digite um valor para [0, {c}]: '))
    l1.append(n1)

for c in range(0, 3):
    n2 = int(input(f'Digite um valor para [1, {c}]: '))
    l2.append(n2)

for c in range(0,3):
    n3 = int(input(f'Digite um valor para [2, {c}]: '))
    l3.append(n3)

print('-=' * 30)

for p in range(0, 3):
    print(f'[{l1[p]:^5}]', end='')
print()

for p in range(0, 3):
    print(f'[{l2[p]:^5}]', end='')
print()

for p in range(0,3):
    print(f'[{l3[p]:^5}]', end='')
print()
