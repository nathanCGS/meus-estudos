#joguinho de advinhação com while
from time import sleep
from random import randint
computador = randint(0, 10)
print('''Sou seu Computador.
Acabei de pennsar em um numero de 0 a 10.
Será que você consegue advinhar qual foi?''')
resp = 'S'
while resp == 'S':
    computador = randint(0, 10)
    print('Acabei de Pensar em outro numero de 0 a 10, qual você acha que foi?')
    acertou = False
    palpite = 0
    while not acertou:
        jogador = int(input('Digite seu palpite: '))
        palpite += 1
        if jogador == computador:
            acertou = True
        if jogador != computador:
            if computador > jogador:
                print('Um pouco mais...')
            else:
                print('um pouco menos...')
    print('Parabens, você acertou co {} tentativas!'.format(palpite))
    print('=--=' * 10)
    resp = str(input('Deseja jogar novamente? [S/N]')).upper()
    print('=--=' * 10)
print('Tudo bem, até mais! Estou finalizando o programa', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
sleep(1)
print('Programa finalizado com sucesso!! :D')



