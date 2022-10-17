#programa que coleta duas notas, faz a media e verifica o resultado, reprovado, recuperação ou aprovado
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('tirando {:.1f} e {:.1f} a media é {:.1f} e o aluno está REPROVADO!.'.format(n1, n2, media))
elif media > 5 and media < 7: #OU 7 > media > 5
    print('tirando {:.1f} e {:.1f} a media é {:.1f} e o aluno está de RECUPERAÇÃO.'.format(n1, n2, media))
elif media > 7:
    print('tirando {:.1f} e {:.1f} a media é {:.1f} e o aluno está APROVADO'.format(n1, n2, media))