cidade = str(input('Qual cidade você nasceu?'))

#forma1 (Na forma um ele não verifica a primeira palavra, ele verifica se existe SANTO no texto todo)
check = 'SANTO' in cidade.upper().strip()
print(check)

#forma2
cidade2 = cidade.strip()
print(cidade2[:5].upper()=='SANTO')