#programa que le a idade e o sexo de várias pessoas. A cada pessoa cadastrada, deve perguntar se quer continuar.
homens = 0
idademulher = 0
idades = 0
while True:
    idade = int(input('Qual sua idade?'))
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        idades += 1
    if sexo == 'F' and idade < 20:
        idademulher += 1
    if sexo == 'M':
        homens += 1
    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Deseja continuar? [S/N]')).strip().upper()
        print('=--=' * 10)
    if decisao == 'N':
        break
print(f'Quantidade de pssoas maiores de idade: {idades}')
print(f'total de homens cadastrados: {homens}')
print(f'Total de mulheres menores que 20 anos: {idademulher}')
