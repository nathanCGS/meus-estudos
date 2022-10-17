#programa que calcula angulo de seno cos e tang.
from math import cos, tan, sin, radians
an = float(input('digite o angulo que deseja: '))
sen = sin(radians(an))
cos = cos(radians(an))
tang = tan(radians(an))
print ('O Seno é: {:.2f} \nO Cosseno é: {:.2f} \nE a Tangente é: {:.2f}'.format(sen, cos, tang))

#ou

'''import math
an = float(input('digite o angulo que deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print ('O Seno é: {:.2f} \nO Cosseno é: {:.2f} \nE a Tangente é: {:.2f}'.format(sen, cos, tang))'''