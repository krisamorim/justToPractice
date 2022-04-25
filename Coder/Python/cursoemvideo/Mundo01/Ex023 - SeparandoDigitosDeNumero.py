numero = int(input('Digite um numero entre 0 e 9999:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: ',u)
print('Dezena: ',d)
print('Centena: ',c)
print('Milhar: ',m)
