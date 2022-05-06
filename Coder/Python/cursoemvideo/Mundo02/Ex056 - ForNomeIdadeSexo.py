somaIdade = 0
maiorIdade = 0
homemMaisVelho = ''
totalMulherMenos20 = 0
for pessoa in range(1,5):
    nome = input('Qual seu nome? ').strip()
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo? M p/ masculino e F p/ feminino ').strip()
    print('{:=^40}\nNome: {}\nIdade: {}\nSexo: {}\n{}'.format(' {} pessoa '.format(pessoa),nome, idade,sexo, '-'*40))
    somaIdade += idade
    if pessoa < 2:
        maiorIdade = idade
    #Verifica se é igua a M maiúsculo ou m minúsculo
    elif sexo in 'Mm'and idade > maiorIdade:
        homemMaisVelho = nome
        maiorIdade = idade
    #Verifica se é igua a F maiúsculo ou F minúsculo
    elif sexo in 'Ff' and idade < 20:
        totalMulherMenos20 += 1

mediaIdade= somaIdade/4
print('A média das idade das 4 pessoa é ',mediaIdade)
if homemMaisVelho == '':
    print('Não foi inserido nenhum homem')
else:
    print('O homem mais velho é o Sr {} com {} anos'.format(homemMaisVelho,maiorIdade))

if totalMulherMenos20 > 1:
    print('Não há mulheres com menos de 20 anos')
else:
    print('Existem {} mulheres com menos de 20 anos de idade'.format(totalMulherMenos20))
