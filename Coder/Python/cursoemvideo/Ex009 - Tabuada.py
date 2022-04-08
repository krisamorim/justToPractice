num = int(input('Digite um número:'))
num2 = 1
print('-'*5)

while (num2<=10):
    if (num2<10):
        print('{} x {:2} = {}'.format(num, num2, num*num2))
    else:
        print('{} x {} = {}'.format(num, num2, num*num2))
    num2 = num2+1