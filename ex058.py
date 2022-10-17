#CALCULADORA iniciante
from time import sleep
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
menu = 0
while menu != 5:
    menu = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
Digite sua opção: '''))
    if menu == 1:
        print('=--=-' * 6)
        print('O resultado é: {} + {} = {}'.format(num1, num2, num1+num2))
        print('=--=-' * 6)
    elif menu == 2:
        print('=--=-' * 6)
        print('O resultado é: {} x {} = {}'.format(num1, num2, num1*num2))
        print('=--=-' * 6)
    elif menu == 3:
        if num1 == num2:
            print('=--=-' * 6)
            print('Os numeros são iguais.')
            print('=--=-' * 6)
        elif num1 > num2:
            print('=--=-' * 6)
            print('Entre {} e {} o maior é: {}'.format(num1, num2, num1))
            print('=--=-' * 6)
        else:
            print('=--=-' * 6)
            print('entre {} e {} o maior é {}'.format(num1, num2, num2))
            print('=--=-' * 6)
    elif menu == 4:
        print('=--=-' * 6)
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        print('=--=-' * 6)
    elif menu == 5:
        print('=--=-' * 6)
        print('Finalizando...')
        print('=--=-' * 6)
        sleep(2)
    else:
        print('=--=-' * 6)
        print('Opção invalida, Escolha um numero entre 1 e 5.')
print('Programa Finalizado! Volte sempre.')