# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')

print('-' * 25)
print('Controle de Terrenos')
print('-' * 25)

area(largura = float(input('LARGURA (m): ')), 
      comprimento = float(input('COMPRIMENTO (m): ')))
