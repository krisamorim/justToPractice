from datetime import date
anoNascimento = int(input('Qual o ano do seu nascimento?\n'))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('MASTER')