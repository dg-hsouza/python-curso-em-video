# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))

cm = medida * 100
mm = medida * 1000

print('A medida de {} metros corresponde a {:.0f} centímetros e {:.0f} milímetros'.format(medida, cm, mm))
