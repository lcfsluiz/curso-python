#!/usr/bin/python3

with open('frutas.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    aux = []
    for x in conteudo:
        x = x.replace('\n', '')
        aux.append(x)
    # print(conteudo)
print(aux)
aux.insert(2, 'pessego')
with open('frutas2.txt', 'w') as arquivo:
    for item in aux:
        arquivo.write('Fruta: {}\n'.format(item.title()))
