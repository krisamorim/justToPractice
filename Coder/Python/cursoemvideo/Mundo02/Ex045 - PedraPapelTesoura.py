from random import randint
from time import sleep
#Cabeçalho
print('{:=^50}'.format(' Jogando Jo Ken Po '))
sleep(1)

#PC escolhendo
print('Computador, o que você escolhe? Pedra, Papel ou tesoura?')
sleep(3)
print('hum...')
sleep(3)
print('Deixe-me pensar um pouco mais')
sleep(3)
computador = randint(0,2)
print('Pronto! Escolhi\n{}'.format('='*50))
sleep(3)

#Humano escolhendo
print('''
Agora é a sua vez:
[0] Pedra
[1] Papel
[2] Tesoura''')
humano = int(input('Digite sua escolha: '))
print('-'*50)
if humano > 2:
    print('Opção inválida')
#Quando humano escolhe pedra (0)
elif humano == 0 and computador == 0:
    print('\033[0:30:43mEmpate!\033[m Você escolheu pedra e o computador também escolheu pedra')
elif humano == 0 and computador == 1:
    print('\033[0:30:41mVocê perdeu\033[m Você escolheu pedra e o computador escolheu papel')
elif humano == 0 and computador == 2:
    print('\33[0:30:42mParabéns!!\033[m Você ganhou! Você escolheu pedra e computaor escolheu tesoura')

#Quando humano escolhe papel (1)
if humano == 1 and computador == 0:
    print('\033[0:30:42mParabéns!!\033[m Você ganhou! Você escolheu papel e computaor escolheu pedra')
elif humano == 1 and computador == 1:
    print('\033[0:30:43mEmpate!\033[m Você escolheu papel e o computador também escolheu papel')
elif humano == 1 and computador == 2:
    print('\033[0:30:41mVocê perdeu\033[m Você escolheu pepel e o computador escolheu tesoura')

#Quando humano escolhe tesoura (2)
if humano == 2 and computador == 0:
    print('\033[0:30:41mVocê perdeu\033[m Você escolheu tesoura e o computador escolheu pedra')
elif humano == 2 and computador == 1:
    print('\033[0:30:42mParabéns!!\033[m Você ganhou! Você escolheu tesoura e computaor escolheu papel')
elif humano == 2 and computador == 2:
    print('\033[0:30:43mEmpate!\033[m Você escolheu tesoura e o computador também escolheu tesoura')

