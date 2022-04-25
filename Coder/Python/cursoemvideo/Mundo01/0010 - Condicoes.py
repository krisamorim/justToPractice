n1 = float(input('Primeira nota? '))
n2 = float(input('Segunda nota? '))
m = (n1+n2)/2
print('A media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média é boa')
else:
    print('Sua media foi menor de 6')
