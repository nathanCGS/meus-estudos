#programa de descontos em produtos onde o usuario coloca a porcentagem de desconto.
preco = float(input('qual o preço do produto?'))
desconto = float(input('quantos % de desconto? '))
novo = preco - (preco*desconto) / 100
print ('O preço atual é {:.2f}R$ e com {:.2f}% de desconto fica {:.2f}R$'.format(preco, desconto, novo))