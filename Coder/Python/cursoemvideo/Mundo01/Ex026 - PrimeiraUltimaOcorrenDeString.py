frase = str(input('Digite uma frase: '))
print('A frase "{}" tem {} letras A'.format(frase,frase.upper().count("A")))
print('A primeira letra A aparece na posiça {}'.format(frase.upper().find("A")+1))
print('A ultima letra A aparece na posiçao {}'.format(frase.upper().rfind("A")+1))