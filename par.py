#!/usr/bin/python3

'''
Faça uma lista de 10 numeros, faça um for na lista
e imprima somente os numeros pares! 
variavel % 2 == 0

'''
qtd = int(input("digite um inteiro: "))

for z in range(qtd):
    if z % 2 != 0:
        print(z)