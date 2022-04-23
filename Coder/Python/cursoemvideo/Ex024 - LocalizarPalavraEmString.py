cidade = str(input('Qual cidade você nasceu?'))

#forma1
check = 'SANTO' in cidade.upper().strip()
print(check)

#forma2
cidade2 = cidade.strip()
print(cidade2[:5].upper()=='SANTO')