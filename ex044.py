from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador =randint(0, 2)
print('-==' * 15)
jogador = int(input('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é sua jogada? '''))
print('-==' * 15)
print('JO')
sleep(0.5)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-==' * 15)
print('o jogador escolheu: {}'.format(itens[jogador]))
print('Computador escolheu: {} '.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('JOGADOR VENCEU!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!')
    else:
        print('JOGADA INVALIDA.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!')
    else:
        print('JOGADA INVALIDA.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!')
    elif jogador == 1:
        print('MAQUINA VENCEU!!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA.')
print('-==' * 15)