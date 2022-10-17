#conversor de medidas
m = float(input('Digite uma distancia em metros:'))
print('a medida de {}m corresponde a\n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm '.format(m, (m / 1000), (m / 100), (m / 10), (m * 10), (m * 100), (m * 1000)))