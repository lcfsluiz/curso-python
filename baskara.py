#!/usr/bin/python3
a = int(input('digite o valor de A: '))
b = int(input('digite o valor de B: '))
c = int(input('digite o valor de C: '))

delta = (b ** 2) - 4 * a * c
baskara1 = (-b + (delta ** 0.5)) / 2 * a

baskara2 = (-b - (delta ** 0.5)) / 2 * a

print('delta:{}, x1:{}, x2{}'.format(delta, baskara1, baskara2))
