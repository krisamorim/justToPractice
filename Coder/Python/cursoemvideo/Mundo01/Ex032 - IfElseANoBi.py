from datetime import date
ano = int(input('Qual ano você quer verificar se é bissexto? (Caso queira analisar o ano atual digite 0\n'))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano ',ano,' é bissexto')
else:
    Print('O ano {} não é bissexto'.format(ano))