print('===' * 10)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('===' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = primeiro
for cont in range(1, 11):
    print(pa, end='... ')
    pa = pa + razao
print('ACABOU!')