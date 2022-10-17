#programa que verifica quantas vezes a letra A apareceu e em qual posição.
nome = str(input('escreva seu nome: ')).strip().lower()
print('Seu nome tem {} letras'.format(len(nome)))
print('A letra: A aparece {} vezes no seu nome.'.format(nome.count('a')))
print('a primeira letra A apareceu na posição: {}'.format(nome.find('a')+1))
print('a ultima letra A apareceu bna posição: {}'.format(nome.rfind('a')+1))