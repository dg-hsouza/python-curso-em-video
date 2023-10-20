# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$'))

if 0 < salario <= 1250:
    aumento = 15
elif salario > 1250:
    aumento = 10
else:
    aumento = 0
    print('Valor inválido')

novo = salario + (salario * aumento / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} com aumento de {}%'.format(salario, novo, aumento))
