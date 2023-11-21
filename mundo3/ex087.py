# Aprimore o desafio anterior, mostrando no final: A) a soma de todos os valores pares digitados
# B) a soma dos valores da terceira coluna C) o maior valor da segunda linha

l1 = []
l2 = []
l3 = []
s1 = s2 = s3 = 0

for c in range(0, 3):
    n1 = int(input(f'Digite um valor para [0, {c}]: '))
    l1.append(n1)
    if n1 % 2 == 0:
        s1 = s1 + n1

for c in range(0, 3):
    n2 = int(input(f'Digite um valor para [1, {c}]: '))
    l2.append(n2)
    if n2 % 2 == 0:
        s2 = s2 + n2

for c in range(0,3):
    n3 = int(input(f'Digite um valor para [2, {c}]: '))
    l3.append(n3)
    if n3 % 2 == 0:
        s3 = s3 + n3

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

print('-=' * 30)

soma = s1 + s2 + s3
print(f'A soma dos valores pares é {soma}.')

col3 = l1[2] + l2[2] + l3[2]
print(f'A soma dos valores da terceira coluna é {col3}.')

print(f'O maior valor da segunda linha é {max(l2)}.')
