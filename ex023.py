#prgrama que verifica se a pessoa nasceu em uma cidade que se inicia com "RIO"
cid = str(input('em que cidade você nasceu: ')).strip()
print(cid[:3].lower() == 'rio')