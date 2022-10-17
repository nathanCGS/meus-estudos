#aumento salario de um funcionario.
sal = float(input('Qual o salário do funcionario? R$ '))
num = float(input('Qual a % de aumento? '))
aument = sal + (num * sal)/100
print ('o salario atual de {:.2f}R$ com {:.0f}% de aumento ficará em {:.2f}R$'.format(sal, num, aument))