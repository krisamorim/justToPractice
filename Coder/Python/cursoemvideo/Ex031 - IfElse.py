dist = float(input('Qual a distância da sua viagem (em KM)?\n'))
cobraMenosDuzentos = 0.5
cobraMaisDuzentos = 0.45

#Usando ternário
preco = dist * cobraMenosDuzentos if dist <= 200 else dist * cobraMaisDuzentos
print('Uma viagem de {}km custa R${:.2f}'.format(dist,preco))
#Usando o IF/ELSE
'''
if dist <= 200.0:
    print('Uma viagem de {}km custa R${:.2f}'.format(dist,dist*cobraMenosDuzentos))
else:
    print('Uma viagem de {}km custa R${:.2f}'.format(dist,dist*cobraMaisDuzentos))
'''