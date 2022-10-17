#exercitanto o comando break
s = qt = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    qt += 1
print(f'A soma dos {qt} números é: {s}')