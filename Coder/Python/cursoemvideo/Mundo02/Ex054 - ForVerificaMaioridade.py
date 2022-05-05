from datetime import date

anoAtual = date.today().year
maior =  0
menor = 0

for c in range(1,8):
    anoNasc = int(input('Digite o ano de nascimento da pessoa: '))
    idade = anoAtual - anoNasc
    if idade < 18:
        print('Menor de idade')
        menor += 1
    else:
        print('Maior de idade')
        maior += 1
print('{:=^40}\nMaior de Idade: {}\nMenor de idade: {}'.format(' TOTAL ', maior,menor))