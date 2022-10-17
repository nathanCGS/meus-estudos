tabuada = int(input('Digite um numero para ver a tabuada: '))
vezes = 1
for c in range(1, 11):
    resultado = tabuada * vezes
    print ('{} x {} = {}'.format(tabuada, vezes, resultado))
    vezes = vezes + 1

#OU

'''tabuada = int(input('Digite um numero para ver a tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(tabuada, c, tabuada*c))'''