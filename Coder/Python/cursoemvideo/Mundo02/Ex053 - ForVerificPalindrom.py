# recebendo o texto, removendo espaços do inicio e do fim, tranforamndo tudo para maiusculo

#Capturando o texto, removendo os espaços do inico e final e transformadno texto para todo maiúsculo
texto = input('Digite o texto: ').strip().upper()

#Separar texto para remover espaços entre palavras
separaFrase = texto.split()

#juntar texto para forma uma unica palavra
juntaFrase = ''.join(separaFrase)

#variavel para salvar a palavra invertida
palavraInversa = juntaFrase[::-1]
'''
#loop para escrever a palavra ao contrártio
for letra in range(len(juntaFrase)-1,-1,-1):
    palavraInversa += juntaFrase[letra]
esse trexo foi substituido por juntaFrase[::-1] que tem o mesmo efeito do loop
'''

print('O texto digitado é: ',texto)
print('Invertido fica assim: ',palavraInversa)
#verificar se a palavra sem espaços é igual ao inverso tab sem espaços
if juntaFrase == palavraInversa:
    print('Portando são palindromos')
else:
    print('Portanto NÃO são palindromos')