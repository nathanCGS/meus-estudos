from datetime import date
ano = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = (nascimento - ano)*-1
print('quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
if idade < 18:
    saldo = idade - 18
    print('Ainda não está na hora de se alistar somente daqui a {}'.format(saldo))
    alistamento = saldo + ano
    print('Seu alistamento sera em'.format(alistamento))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
    alistamento = ano - saldo
    print('Seu alistamento foi em {}'.format(alistamento))