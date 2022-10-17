#programa que calcula o IMC de uma pessoa
peso = float(input('Qual é seu peso? (KG): '))
altura = float(input('Qual é sua altura? (M): '))
imc = peso / (altura * altura)
print('Seu imc é {:.1f}'. format(imc))
if imc < 18.5:
    print('Seu imc é {:.1f} e você tá abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu imc é {:.1f} e você tá no peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu imc é {:.1f} e você tá com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu imc é {:.1f} e você tá com obesidade'.format(imc))
else:
    print('Seu imc é {:.1f} e você tá com Obesidade morbida'.format(imc))