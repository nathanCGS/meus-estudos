# jogo do impa ou par
from random import randint
from random import randint

print('=--=' * 7)
print('VAMOS JOGAR PAR OU IMPAR')
print('=--=' * 7)
v = 0
while True:
    jogador = int(input('Digite um valor:'))
    pc = randint(0, 10)
    poui = ' '
    resultado = pc + jogador
    while poui not in 'PI':
        poui = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print('------' * 8)
    print(f'Voce jogou {jogador} e computador jogou {pc} total de {resultado}', end=' ')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR')
    print('------' * 8)
    if poui == 'P':
        if resultado % 2 == 0:
            print('Você venceu!!')
            print('==-==' * 8)
            v += 1
        else:
            print('Você perdeu...')
            print('==-==' * 8)
            break
    if poui == 'I':
        if resultado % 2 != 0:
            print('Você Ganhou!!')
            print('==-==' * 8)
            v += 1
        else:
            print('Você perdeu...')
            print('==-==' * 8)
            break

    print('Vamos jogar novamente!!')
    print('==-==' * 8)
print(f'GAMER OVER! Você venceu {v} vezes')
