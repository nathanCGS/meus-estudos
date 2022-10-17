#programa pede pro usuario digitar dois numeros e verifica qual é maior ou se são iguais
n1 = float(input('Primeiro numero: '))
n2 = float(input('Segundo numero: '))
if n1 > n2:
    print('O PRIMEIRO numero é maior!')
elif n1 < n2:
    print('O SEGUNDO numero é maior')
else:
    print('Os numeros são IGUAIS!')
