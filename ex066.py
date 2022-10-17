#SUPER TABUADA
c = 1
while True:
    n = int(input('Digite um número: '))
    if n <= -1:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('=-=' * 10)
print('Programa finalizado...')