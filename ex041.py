#programa de identificar triangulos
lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('Os segmentos acima PODEM FORMAR um triangulo EQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Os segmentos acima PODEM FORMAR um triangulo ISCALENO')
    else:
        print('Os segmentos acima PODEM FORMAR um triangulo ISÓSCELES ')
else:
    print('Os segmentos não podem formar um triangulo.')