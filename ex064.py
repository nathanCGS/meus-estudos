#programa que le vários números inteiros pelo teclado. No final da execução, mostra a média entre todos os valores e qual foi o maior e o menor valores lidos.
decisao = 'S'
qt = 0
soma = 0
menor = 0
menor = 0
while decisao == 'S':
    n = int(input('Digite um numero: '))
    qt = qt + 1
    soma = soma + n
    if qt == 1:
        maior = menor = n
    else:
        if maior > n:
            maior = n
        if menor < n:
            menor = n
    decisao = str(input("Deseja continuar? [S/N]")).upper()
media = soma / qt
print('Você digitou {} e sua média foi: {:.2f}'.format(qt, media))
print('O maior numero foi: {} e o menor foi: {}'.format(maior, menor))
