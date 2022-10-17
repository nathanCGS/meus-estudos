# programa que separa multiplos de 3, verifica qquantos são e soma todos.
tot = 0
num = 0
for cont in range(1, 501):               #for cont in range(1, 501, 2)
    if cont % 3 == 0 and cont % 2 != 0:  #if cont % 3 == 0:
        num += 1
        tot += cont
print('a soma de todos os {} valores solicitados é {}'.format(num, tot))
