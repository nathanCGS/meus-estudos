dist = float(input('qual a distancia da viagem? '))
print('você está prestes a começar uma viagem de {:.1f}Km'.format(dist))
if dist <= 200:
    val = 0.5 * dist
    print('o valor da sua viagem vai ser de: {:.2f}R$'.format(val))
else:
    val = 0.45 * dist
    print('o valor da sua viagem vai ser de: {:.2f}R$'.format(val))

##pode usar tambem: val = 0.5 * dis if dist <= 200 else dist * 0.45