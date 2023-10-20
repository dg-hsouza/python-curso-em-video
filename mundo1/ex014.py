# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

cel = float(input('Informe a temperatura em ºC: '))
fah = (cel * 9/5) + 32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(cel, fah))
