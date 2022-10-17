#programa que verifica primeiro e ultimo nome de uma pessoa
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('seu primeio nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))