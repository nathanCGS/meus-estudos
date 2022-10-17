n = int(input('Digite um numero: '))
soma = 0
for cont in range(1, n + 1):
    if n % cont == 0:
        soma = soma + 1
if soma > 2:
    print('O numero {} foi divisivel {} vezes e não primo.'.format(n, soma))
else:
    print('{} é um numero primo'.format(n))