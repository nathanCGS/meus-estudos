#identificando sexo com while
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'FfMm':
    sexo = str(input('Opção invalida. Digite seu sexo novamente [M/F]: '))
print('Sexo {} Registrado.'.format(sexo.upper()))