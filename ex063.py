#somador de X numeros
n = int(input('Digite um numero para somar ou [999] para sair: '))
s = 0
qt = 0
while n != 999:
    s = s + n
    qt = qt + 1
    n = int(input('Digite um numero para somar ou [999] para sair: '))
print('A soma dos {} valores é: {}'.format(qt, s))