#pode ser feito tbm importando uma biblioteca import math e usar o comando math.trunk()
#ou importar somente o trunc usando from math import trunc exemplo abaixo.
#ou usar o comando int()num

import math
from math import trunc
'''num = float(input('escreva um numero: '))
print ('o numero {} em sua porção inteira é {}'.format(num, math.trunc(num)))'''

num = float(input('escreva um numero: '))
print ('o numero {} em sua porção inteira é {}'.format(num, int(num)))

'''num = float(input('escreva um numero: '))
print('o numero {} em sua porção inteira é {:.0f}'.format(num, num))'''