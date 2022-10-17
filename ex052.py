#Exercicios que verificam se a frase é um polindromo
frase = str(input('Digite uma frase: ')).strip().upper() #TIREI OS ESPAÇOS E COLOQUEI TUDO PRA MAIUSCULO
palavras = frase.split() #SEPAREI EM LISTA
junto = ''.join(palavras) # JUNTEI A LISTA PRA ELIMINAR OS ESPAÇOS
inverso = ''
for letra in range(len(junto) -1, -1, -1): #FUI DA ULTIMA LETRA ATE A PRIMEIRA VOUTANDO -1
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um políndromo!')
else:
    print('A frase digitada não é um políndromo!')