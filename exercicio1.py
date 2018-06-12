#!/usr/bin/python3
nomes = ['daniel', 'pedro', 'maria', 'renata']
nomes[0] = 'joao'

nomes.append('Rick')

nomes.insert(0, 'patrão')

for nome in nomes:
    print("Seja bem vindo {}".format(nome.title()))

while len(nomes) > 0:
    print(nomes)
    nomes.pop()
print(nomes)
