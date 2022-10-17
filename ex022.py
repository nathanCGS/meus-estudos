#manipulando texto, deixei dois exemplos abaixo para que eu posso usar ambos e me aprimorar usando o que eu achar melhor
nome = str(input('escreva seu nome completo: ')).strip()
print('seu nome completo em letras maiusculas é: {}'.format(nome.upper()))
print('seu nome completo em letras minustulas é: {}'.format(nome.lower()))
print('seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras. '.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))