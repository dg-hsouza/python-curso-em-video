# Dentro do pacote utilidadesCeV que criamos no ex 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.

import moeda
import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
