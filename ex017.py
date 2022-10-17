#calculando comprimento da hipotenusa.
#primeiro usando a formula matemática e o segundo importando um módulo.
cato = float(input('Cateto oposto: '))
cata = float(input('Cateto adjacente: '))
print('A hipotenusa mede {:.2f}'.format((cata ** 2 + cato ** 2) ** 0.5))

#ou

'''from math import hypot
cato = float(input('Cateto oposto: '))
cata = float(input('Cateto adjacente: '))
print('a hipotenusa mede {:.2f}'.format(hypot(cato, cata)))'''