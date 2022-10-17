#programa que simula uma loja.
preco = float(input('Preço das compras. R$'))
print('==-' * 15)
pagamento = int(input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual opção deseja? '''))
print('==-' * 15)
if pagamento == 1:
    valor = preco - (preco * 10 / 100)
    print('O valor a ser pago é de {:.2f}R$'.format(valor))
elif pagamento == 2:
    valor = preco - (preco * 5 / 100)
    print('O valor a ser pago é de {:.2f}R$'.format(valor))
elif pagamento == 3:
    valor = preco / 2
    print('o valor a ser pago é 2x de {:.2f}R$'.format(valor))
elif pagamento == 4:
    valor = preco + (preco * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    print('O o valor a ser pago é de: {:.2f}R$ sendo {}x de {:.2f}R$ COM JUROS. '.format(valor,parcela, valor/parcela))
else:
    print('Opção invalida, tente novamente.')
print('==-' * 15)