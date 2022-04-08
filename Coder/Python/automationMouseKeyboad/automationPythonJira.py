from time import time
#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python
import pyautogui
import time
import os
os.chdir(r'C:\Users\Kris.Furtado\OneDrive - Deliver IT\Documentos\Code\justToPractice\Python\automationMouseKeyboad')

time.sleep(3)

#add analise de tarefas 6h na segunda
#mover o mouse para baixo
pyautogui.click(x=359, y=804)
#clicar no botão +
addJira = pyautogui.locateOnScreen('addJira.png')
pyautogui.click(addJira)


time.sleep(10)

#Clicar no card de registrar report da segunda
pyautogui.doubleClick(x=387, y=421)
time.sleep(3)

#Clicar no menu dropdown
pyautogui.click(x=1127, y=589)
#Digitar apresentação
pyautogui.write('apresenta')
#aguardar
time.sleep(2)
#ir para botão update e dar enter
pyautogui.press(['enter', 'tab', 'tab', 'enter'])




#P/ confirmar card revisão de quadro kanban da SEGUNDA
pyautogui.doubleClick(383, 678)

time.sleep(2)
pyautogui.click(x=1124, y=670)

time.sleep(2)
pyautogui.write('apresenta')

time.sleep(2)
pyautogui.press(['enter','tab', 'tab', 'enter'])

#P/ confirmar card revisão de quadro kanban da TERÇA
pyautogui.doubleClick(x=612, y=656)

time.sleep(2)
pyautogui.click(x=1124, y=670)

time.sleep(2)
pyautogui.write('gest')

time.sleep(2)
pyautogui.press(['enter','tab', 'tab', 'enter'])

#P/ confirmar card revisão de quadro kanban da QUARTA
pyautogui.doubleClick(x=835, y=675)

time.sleep(2)
pyautogui.click(x=1124, y=670)

time.sleep(2)
pyautogui.write('gest')

time.sleep(2)
pyautogui.press(['enter','tab', 'tab', 'enter'])


#P/ confirmar card revisão de quadro kanban da QUINTA ATENÇÂÂÂOOOO
pyautogui.doubleClick(x=996, y=682)

time.sleep(2)
pyautogui.click(x=1124, y=670)

time.sleep(2)
pyautogui.write('gest')

time.sleep(2)
pyautogui.press(['enter','tab', 'tab', 'enter'])


#P/ confirmar card revisão de quadro kanban da SEXTA
pyautogui.doubleClick(x=1154, y=670)

time.sleep(4)
pyautogui.click(x=1125, y=663)

time.sleep(2)
pyautogui.write('gest')

time.sleep(2)
pyautogui.press(['enter','tab', 'tab', 'enter'])

#proxima pagina
buttonProx = pyautogui.locateOnScreen('proxPage.png')
pyautogui.click(buttonProx)

# pyautogui.write('Digite seu texto aqui')
#pyautogui.move()

#mover mouse p/ uma posição especifica
#pyautogui.moveTo()

#Arrastar
#pyautogui.drag()