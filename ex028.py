#programa de radar eletronico
velocidade = int(input('Qual a velocidade do carro?'))
if velocidade <= 80:
    print('==-' * 20)
    print('Voce esta na velocidade permitida, tenha uma otima viagem!!')
    print('==-' * 20)
else:
    print('****' * 15)
    multa = (velocidade - 80) * 7   #7 reais por km acima do limite.
    print('Você está acima da velocidade permitida de: 80Km/h \nE tera que pagar uma multa de {}R$'.format(multa))
    print('****' * 15)