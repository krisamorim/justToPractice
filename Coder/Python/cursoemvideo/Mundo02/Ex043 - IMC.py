peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Uma pessoa com {}kg e com {}m de altura, tem imc de {:.2f} está classificada como {}'.format(peso, altura, imc,'Abaixo do peso'))
elif imc < 25:
    print('Uma pessoa com {}kg e com {}m de altura, tem imc de {:.2f} está classificada como {}'.format(peso, altura, imc,'Peso ideal'))
elif imc < 30:
    print('Uma pessoa com {}kg e com {}m de altura, tem imc de {:.2f} está classificada como {}'.format(peso, altura, imc,'Sobrepeso'))
elif imc < 40:
    print('Uma pessoa com {}kg e com {}m de altura, tem imc de {:.2f} está classificada como {}'.format(peso, altura, imc,'Obesidade'))
else:
    print('Uma pessoa com {}kg e com {}m de altura, tem imc de {:.2f} está classificada como {}'.format(peso, altura, imc,'Obesidade mórbida'))