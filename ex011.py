#programa que vê largura a altura de uma parede e faz o calculo e sera usado 1litro de tinta para cada 2m²
l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
area = l * a
print('sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(area/2))
