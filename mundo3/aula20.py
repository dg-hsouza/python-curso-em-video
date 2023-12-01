def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

def soma(a, b):
    s= a + b
    print(s)

def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

titulo(' Testando ')
soma(1, 2)
soma(3, 4)
soma(5, 6)
soma(7, 8)
soma(9, 10)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
