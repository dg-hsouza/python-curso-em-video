# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num2 = int(input('Digite um número entre 0 e 20: '))
    if num2 >= 0 and num2 <= 20:
        print(f'O número digitado foi {num1[num2]}!')
        break
    else:
        print('Valor inválido! Tente novamente.')
