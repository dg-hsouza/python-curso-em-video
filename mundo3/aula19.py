# Criando um dicionário
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

# Retorna todos os valores (valor)
print(filme.values())

# Retorna todos os elementos (chave)
print(filme.keys())

# Retorna todos os valores e elementos (iten)
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')
print('-=' * 30)

pessoas = {'nome': 'Diogo', 'sexo': 'M', 'idade': 20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

del pessoas['sexo']
pessoas['peso'] = 75.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 30)

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
