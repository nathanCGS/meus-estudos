#programa que le os dados e faz uma analise dos dados coletados.
soma = 0
velho = 0
nomevelho = ''
idademulher = 0
menorque20 = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).upper()
    soma = soma + idade
    if idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == 'F':
        idademulher = idade
        if idademulher < 20:
            menorque20 = menorque20 + 1
media = soma / 4
print('A media de idade do grupo é de: {} '.format(media))
print('O homem mais velho tem {} e se chama {}.'.format(velho, nomevelho))
print('Ao todo sao {} mulheres menores que 20 anos.'.format(menorque20))




