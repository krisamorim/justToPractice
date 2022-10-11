#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python

import pyautogui
from time import sleep

sleep(5)

for count in range(1,4):
    print("Acionando propaganda")
    #clicar na propaganda
    pyautogui.click(1568, 665)
    print("Esperando propaganda")
    #esperar propaganda
    sleep(33)
    print("Fechar propaganda")
    #Fechar propaganda
    pyautogui.click(1423, 63)
    print("Fechando propaganda2")
    #fechar propaganda2
    pyautogui.click(1860,60)
    sleep(2)


#coordenadas = pyautogui.position()
#print(coordenadas)
# pyautogui.click(posicaoVariavel)
# sleep(1)
# xx = int(coordenadas[0])+80
# yy = int(coordenadas[1])+100
# #Clicar
# pyautogui.click(xx, yy)