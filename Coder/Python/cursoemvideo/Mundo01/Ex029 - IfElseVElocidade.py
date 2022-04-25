velAtual = float(input('QUal a velocidade atual?\n'))
calcMulta = (velAtual-80.0)*7.00
if velAtual > 80.0:
    print('Você foi \033[31mmultado\033[m.\nA multa custa: R${:.2f}'.format(calcMulta))
