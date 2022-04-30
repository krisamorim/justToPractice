from datetime import date
anoAtual = date.today().year
anoNascimento = int(input('Qual ano do seu nascimento?\n'))
anosIdade = anoAtual - anoNascimento
if anosIdade <= 17:
    print('Você tem {} faltam {} anos para o seu alistamento'.format(anosIdade,18-anosIdade))
elif anosIdade > 18:
    print('Você tem {} e por isso deveria ter se alistado há {} anos'.format(anosIdade,anosIdade-18))
else:
    print('Esse ano você completa 18 anos e por isso se alistar ainda esse ano')
