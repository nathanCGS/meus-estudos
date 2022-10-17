#programa que le 7 idades e verifica quantas sao menores de idade e quantas sao maiores
from datetime import date
menores = 0
maiores = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('Ao todos tivemos {} maiores de idade'.format(maiores))
print('E tambem tivemos {} menores de idade'.format(menores))

v