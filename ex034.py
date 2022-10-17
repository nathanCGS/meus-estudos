#programa que verifica se os segmentos podem formar triangulos.
print ('-=--' * 7)
print('Analisador de triangulos!')
print ('-=--' * 7)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input(('terceiro segmento: ')))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulos!')