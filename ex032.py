#programa que verifica o maior e menor numero
v1 = int(input('digite o primeiro valor: '))
v2 = int(input('digite o segundo valor:'))
v3 = int(input('digite o terceiro valor:'))
#verificando quem é o menor
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
#verificando quem é o maior
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O maior numero é: {}'.format(maior))
print('O menor numero é: {}'.format(menor))
