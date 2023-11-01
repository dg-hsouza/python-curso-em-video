# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# EX: apos a sopa / a sacada da casa / a torre da derrota / o lobo ama o bolo / anotaram a data da maratona

frase = str(input('Digite uma frase: ')).upper().strip()

palavra = frase.split()
junto = ''.join(palavra)
#inverso = ''
inverso = junto[ : : -1]

print('Você digitou a frase {}'.format(frase))

#for letra in range(len(junto) - 1, -1, -1):
#    inverso = inverso + junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

