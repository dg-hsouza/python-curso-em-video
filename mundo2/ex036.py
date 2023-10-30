# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou
# então o empréstimo será negado.

valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anospagar = int(input('Quantos anos de financiamento? '))

ano = anospagar * 12
prestacao = valorcasa / ano
saldo = (salario / 100 * 30)

print('O valor da casa é R${:.2f}, em {} anos, cada prestação vai ser de R${:.2f}'.format(valorcasa, anospagar, prestacao))
print('Com o salário R${:.2f}, 30% da renda equivale a R${:.2f}'.format(salario, saldo))

if prestacao > saldo:
    print('Empréstimo NEGADO')
elif prestacao <= saldo:
    print('Empréstimo APROVADO')
