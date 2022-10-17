#programa que le nome e o preço de vários produtos
totc = produto = barato = cont = 0
nomep = ' '
while True:
    produt = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    resp = ' '
    totc += preço
    if preço > 1000:
        produto += 1
    if cont == 1 or preço < barato:
        barato = preço
        nomep = produt
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print(f'O total da compra foi de {totc:.2f}')
print(f'temos {produto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomep} que custou {barato:.2f}')