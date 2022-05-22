from random import randint
numSorteado = randint(0,10)
numEscolhido = int(input('Digite o número de 1 a 10 que você acha que foi sorteado: '))
tentativas = 1
while numEscolhido != numSorteado:
    numEscolhido = int(input('\033[1:31mErrado!!\033[m Tente novamente\nDigite o número de 1 a 10 que você acha que foi sorteado: '))
    tentativas += 1

if tentativas < 2:
    print('\033[:42mParabéns!!!\033[m Você acertou de primeira.\nO número sorteado foi {}'.format(numSorteado))
elif tentativas < 3:
    print('\033[32:41mParabéns!!!\033[m Você acertou com menos de 3 tentativas\nO número sorteado foi {}'.format(numSorteado))
else:
    print('Nossa!!! Finalmente em!! Você acertou depois de {} tentativas \033[32:41mParabéns!!!\033[m você acertou.\nO número sorteado foi {}'.format(tentativas, numSorteado))
