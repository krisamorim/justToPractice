#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python

import pyautogui
from time import sleep
import os
os.chdir(r'C:\Users\Kris.Furtado\OneDrive - Deliver IT\Área de Trabalho\Docs\Documentos\Code\justToPractice\Coder\Python\automationMouseKeyboad')

#--------------capturar posição das imagens dos dias da semana-------------
posicaoSegunda = pyautogui.locateOnScreen('./seg.png')
posicaoTerca = pyautogui.locateOnScreen('./ter.png')
posicaoQuarta = pyautogui.locateOnScreen('./qua.png')
posicaoQuinta = pyautogui.locateOnScreen('./qui.png')
posicaoSexta = pyautogui.locateOnScreen('./sex.png')
posicaoProximPagina = pyautogui.locateOnScreen('./proxPage.png')

#---------Criar funções para as ações diárias dos cards pré definidos--------
#Primeiro card Registrar Report Diario
def clickPrimeiroCard_Segunda():
    #clicar na imagem
    pyautogui.click(posicaoVariavel)
    #pegar as coordenadas
    coordenadas = pyautogui.position()
    print(coordenadas)
    #aguardar 1 segundo
    sleep(1)
    #correr para a direita até o meio do card
    xx = int(coordenadas[0])+80
    #descer até o meio do primeiro cars
    yy = int(coordenadas[1])+100
    #Clicar
    pyautogui.click(xx, yy)
    return(xx,yy)
def registrarCardStatusReportDiario():
    sleep(3)
    pyautogui.press(['tab','tab','tab','tab','tab'])
    sleep(3)
    pyautogui.write('gest')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press(['tab', 'tab', 'enter'])
    sleep(1)

#Segundo card Daily
def clickSegundoCard_Segunda():
    #clicar na imagem
    pyautogui.click(posicaoVariavel)
    #pegar as coordenadas
    coordenadas = pyautogui.position()
    print(coordenadas)
    #aguardar 1 segundo
    sleep(1)
    #correr para a direita até o meio do card
    xx = int(coordenadas[0])+80
    #descer até o meio do primeiro cars
    yy = int(coordenadas[1])+270
    #Clicar
    pyautogui.click(xx, yy)
    return(xx,yy)
def registrarCardDaily():
    sleep(3)
    pyautogui.press(['tab','tab','tab','tab','tab'])
    sleep(3)
    pyautogui.write('reuni')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press(['tab', 'tab', 'enter'])
    sleep(1)

#terceiro card - Revisar quadro kanban
def clickTerceiroCard_Segunda():
    #clicar na imagem
    pyautogui.click(posicaoVariavel)
    #pegar as coordenadas
    coordenadas = pyautogui.position()
    print(coordenadas)
    #aguardar 1 segundo
    sleep(1)
    #correr para a direita até o meio do card
    xx = int(coordenadas[0])+80
    #descer até o meio do primeiro cars
    yy = int(coordenadas[1])+340
    #Clicar
    pyautogui.click(xx, yy)
    return(xx,yy)
def registrarCardRevisaKanban():
    sleep(3)
    pyautogui.press(['tab','tab','tab','tab','tab'])
    sleep(3)
    pyautogui.write('gest')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press(['tab', 'tab', 'enter'])
    sleep(1)


#---------------------Criar funções para um dia completo---------------------
def executar1diaDosCardsPREdefinidos():
    clickPrimeiroCard_Segunda()
    registrarCardStatusReportDiario()
    clickSegundoCard_Segunda()
    registrarCardDaily()
    clickTerceiroCard_Segunda()
    registrarCardRevisaKanban()

for count in range(1,3):
    for c in range(1, 6):
        if c == 1:
            posicaoVariavel = posicaoSegunda
        if c == 2:
            posicaoVariavel = posicaoTerca
        if c == 3:
            posicaoVariavel = posicaoQuarta
        if c == 4:
            posicaoVariavel = posicaoQuinta
        if c == 5:
            posicaoVariavel = posicaoSexta
        print('Começando {}º dia, faltam {} dias'.format(c, 5 - c))
        executar1diaDosCardsPREdefinidos()
    pyautogui.click(posicaoProximPagina)
    sleep(5)
    print(count, 'ª semana ja foi')