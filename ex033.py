#programa que faz aumento no salario de acordo com seus ganhos.
salario = float(input('informe o salario do funcionario: '))
if salario <= 1250:
    aumento = salario + (salario * 15) / 100
    print('O trabalhador ganhava {:.2f}R$ e seu novo salario é de {:.2f}R$'.format(salario, aumento))
else:
    aumento = salario + (salario * 10) / 100
    print('O trabalhador ganhava: {:.2f}R$ e seu novo salario é de {:.2f}R$'.format(salario, aumento))