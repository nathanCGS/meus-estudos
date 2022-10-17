#programa que verifica se a pessoa pode fazer um emprestimo e comprar para compra casa.
vcasa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o seu salario: R$'))
pagar = int(input('em quanto tempo deseja pagar? '))
mensalidade = vcasa / (pagar * 12)
minimo = salario * 30 / 100
if mensalidade > minimo:
    print('sua mensalidade ficaria no valor de: {:.2f}R$ e excede {:.2f}R$ que é 30% do seu salario.'.format(mensalidade, minimo))
    print('EMPRESTIMO NEGADO.')
else:
    print('para pagar uma casa de {:.2f} em {} a mensalidade fica no valor de {:.2f}.'.format(vcasa, pagar, mensalidade))
    print('EMPRESTIMO CONCEDIDO!')