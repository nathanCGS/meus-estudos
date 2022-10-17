#calculando o valor do aluguel, 60 reais por dia e 0.15 centavos por Km rodado.
dias = int(input('Quantos dias alugados?'))
km = float(input('quantos Km Rodados?'))
tot = (dias * 60) + (km * 0.15)
print ('o total a pagar é: {:.2f}'.format(tot))