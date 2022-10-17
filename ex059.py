# programa que calcula fatorial, no caso do python eu poderia tbm usar o modulo math: from math import factorial
# ficaria bem mais facil, mas como estou praticando prefiro fazer assim.
from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial. '))
f = 1
c = n
print('o fatorial de {}! é: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)

#ou

n = int(input('Digite um numero para calcular o seu fatorial. '))
f = 1
print('o fatorial de {}! é: '.format(n), end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print(f)