#Simulador de caixa eletronico
valor = int(input('Qual valor Deseja sacar? R$'))
ced = 50
totced = valor
cont = 0
while True:
    if totced >= ced:
        totced = totced - ced
        cont = cont + 1
    else:
        if cont >= 1:
            print(f'Total de {cont} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        cont = 0
        if totced == 0:
            break
