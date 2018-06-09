#!/usr/bin/python3
# read() ler arquivo inteiro
# readline ler linha do arquivo
# seek()
# readlines ler arquivo inteiro como lista
# w r a
# with open('frutas.txt', 'r') as arquivo:
# .strip().replace('', '')
# texto.split()

'''Abrir um arquivo não existente, e adicionar
nomes em um loop ate que o usuario digite sair
'''
with open('nomes.txt', 'a') as arquivo:
    while True:
        nome = input("Digite um nome: ")
        if nome.lower() == 'sair':
            break
        arquivo.write(nome + "\n")

# with open('frutas.txt', 'a+') as arquivo:
#     fruta = input("digite a fruta: ")
#     arquivo.write(fruta + '\n')
