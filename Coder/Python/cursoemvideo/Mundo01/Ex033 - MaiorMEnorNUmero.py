n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o primeiro número: '))
n3 = int(input('Digite o primeiro número: '))
#MAIOR
maior = n3;
menor = n1
if n1 > n2 and n1 >n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

#MENOR
if n3 < n2 and n3 < n1:
    menor = n3;
if n2 < n1 and n2 < n3:
    menor = n2
print('O maior número é {}\nO menor número é {}'.format(maior, menor))
