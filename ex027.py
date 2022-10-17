#jogo de advinhar numero.
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um numero entre 0 e 5, tente advinhar!!') #faz o computador sortear um numero
print('-=-' * 18)
jogador = int(input('Digite um numero entre 0 e 5: ')) #usuario tenta advinhar o numero sorteado
print('---' * 10)
print('PROCESSANDO...')
print('---' * 10)
sleep(2)
if computador == jogador:
    print('Parabens, eu tambem escolhi {}, VOCE GANHOU!!!'.format(jogador))
else:
    print('eu escolhi {} e não {}, VOCE PERDEU!!!'.format(computador, jogador ))