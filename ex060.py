#gerador de P.A
primeiro = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
cont = 1
pa = primeiro
while cont <= 10:
    print(pa, end=' - ')
    pa = pa + razao
    cont = cont + 1
print('FIM...')