# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))

aumento = 15
novosalario = salario + (salario / 100 * aumento)

print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, aumento, novosalario))
