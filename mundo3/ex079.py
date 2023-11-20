# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
# já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

valor = []

while True:
    num = (int(input('Digite um valor: ')))
    if num not in valor:
        valor.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    seguir = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if seguir == 'N':
        break
    while seguir not in 'S':
        print('Opção inválida. Tente novamente...')
        seguir = str(input('Quer continuar? [S/N] ')).upper().split()[0]

print('-=' * 30)
print(f'Você digitou os valores {sorted(valor)}')
