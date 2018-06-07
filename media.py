#!/usr/bin/python3
# Leia um nome de um aluno, e leia duas notas, calcule a media
# do aluno e imprima  nome do aluno e media

aluno = input('Digite um nome de um aluno: ')
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
falta = int(input("digite a quantidade de faltas: "))
media = (n1 + n2) / 2
if media >= 7 and falta <= 4:
    resultado = "aprovado!"
else:
    resultado = "reprovado!"

print("O aluno {} teve a media de \
    {} e foi {}".format(aluno, media, resultado))
