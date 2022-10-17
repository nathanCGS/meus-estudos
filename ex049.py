#programa que verifica a quantidade de numeros pares digitados e soma eles.
soma = 0
pares = 0
for c in range(1, 7):
    numero = int(input('Escreva o {}° numero: '.format(c)))
    if numero % 2 == 0:
        soma = soma + numero
        pares = pares + 1
print('A soma entre os {} numeros pares digitados é {}.'.format(pares, soma))