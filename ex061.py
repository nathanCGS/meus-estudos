#super gerador de P.A
primeiro = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
cont = 1
pa = primeiro
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(pa, end=' - ')
        pa = pa + razao
        cont = cont + 1
    print('PAUSA...')
    mais = int(input('Quantos termos que mostrar a mais?'))
print('A progressão foi finalizada e mostrou {} termos.'.format(total))