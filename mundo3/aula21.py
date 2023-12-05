help(print)
help(len)
help(input)
print('-=' * 30)

print(input.__doc__)
print('-=' * 30)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Diogo Henrique de Souza
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c = c + p
    print('FIM!')

contador(2, 10, 2)

help(contador)
print('-=' * 30)

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar()
somar(b=4, c=2)
print('-=' * 30)

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print('-=' * 30)

def somar(a=0, b=0, c=0):
    s = a+ b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
print('-=' * 30)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')
