frase='curso em video Python'
fraseComEspaco = ' Curso em video Python com espaço no inicio e no final da frase '
mostraCaracterposicaoNOVE = frase[9]
deNoveAteVinteUM = frase[9:21]
daTrezeAteFinal = frase[13:]
deNoveAteVinteeumPulando2caracter = frase[9:21:3]
dividir = frase.split()
maiusculo = frase.upper()
minusculo = frase.lower()
localizarLetraM = frase.find("m")
quantidade = len(frase)
espaco = frase.strip()
print('O caracter da posição 9 é o: {}\nA frase do caracter 9 ao 21 fica assim: {}\nA frase do caracter 13 até o final fica assim: {}\nA frase do caracter 9 ao 21, pulando 2 caracter por vez fica assim: {}\ndividir: {}\nmaiúsculo: {}\nminusculo: {}\nA letra M começa a partir da  posição {}\nA quantidade de caracteres em "{}" é {}\n'.format(mostraCaracterposicaoNOVE,deNoveAteVinteUM,daTrezeAteFinal,deNoveAteVinteeumPulando2caracter,dividir, maiusculo, minusculo, localizarLetraM,frase ,quantidade))

print('Podemos colocar a primeira letra em maiúsculo, ficando assim: {}\nPodemos substituir a palavra Python por Java, então a frase fica assim: {}\n'.format(frase.capitalize(),frase.replace('Python', 'Java')))

print('Na frase "{}" (que tem espaços no inicio e no final), existem {} caracteres mas, se removermos os espaços ela fica somente com {} caracteres'.format(fraseComEspaco, len(fraseComEspaco), len(fraseComEspaco.strip())))

print('Na frase "{}" tem a palavra espaço? {}\n'.format(fraseComEspaco,'espaço' in fraseComEspaco))

print('Podemos substituir os espaços na frase "{}" por vírgula e ficara assim: {}\nTambém podemos colocar em maiúculo a primeira letra de cada palavra, ficando assim: {}'.format(frase,",".join(frase.split()), ",".join(frase.title().split())))


