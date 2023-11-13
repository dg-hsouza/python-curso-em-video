lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Tuplas são imutáveis
#lanche[1] = 'Refrigerante'

# Os 'for' abaixo são a mesma coisa, eles dão o mesmo resultado.
for comida in lanche: # Maneira mais simples, não mostra a posição.
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)): # Mostra a posição usando o 'range'.
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche): # Mostra a posição usando o 'enumerate', precisa de 2 variáveis mo 'for'.
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche)) # Para mostrar em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c)) # Tamanho de 'c'.
print(c.count(5)) # Quantas vezes aparece '5'.
print(c.index(8)) # Em que posição está o '8'.
print(c.index(5, 1)) # Em que posição está o '5' a partir da posição '1'.

pessoa = ('Diogo', 20, 'M', 75.5) # Em python, as tuplas armazenam dados de diferentes tipos.
print(pessoa)
del(pessoa) # Para apagar da memória
