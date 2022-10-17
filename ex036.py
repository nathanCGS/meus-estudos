#calculadora que modifica o numero de acordo com as tres opçoes: binario, octal, hexadecimal
n = int(input('Digite um número inteiro: '))
print('-=--' * 10)
print('''Escolha uma das bases para conversão:
[1] Converter para binario.
[2] Converter para octal.
[3] Converter para hexadecimal''')
print('-=--' * 10)
escolha = int(input('Escolha uma opçao:'))
if escolha == 1:
    print('O numero: {} convertido para binario é: {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O numero {} convertido para octal é: {} '.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O numero {} convertido para hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('Escolha invalida!')