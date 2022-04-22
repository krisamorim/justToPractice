from time import time
#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python
import pyautogui
import time
import os
os.chdir(r'C:\Users\Kris.Furtado\OneDrive - Deliver IT\Documentos\Code\justToPractice\Python\automationMouseKeyboad')

time.sleep(10)

for i in range(2):
    #CTRL+C
    #pyautogui.keyDown('ctrl')
    #pyautogui.press(['c'])
    #pyautogui.keyUp('ctrl')
    pyautogui.hotkey('ctrl','c')

    #ir p/ navegador
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #descer
    pyautogui.press(['down', 'down', 'down', 'down'])

    #Clicar em add
    buttonAdd = pyautogui.locateOnScreen('AddButton.png')
    pyautogui.click(buttonAdd)

    #Aguardar 1seg
    time.sleep(1)

    #CTRL+V da data
    #pyautogui.keyDown('ctrl')
    #pyautogui.press(['v'])
    #pyautogui.keyUp('ctrl')
    pyautogui.hotkey('ctrl','v')

    #volta p/ excel
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #vai para celula da hora inicial
    pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left', 'left'])

    #CTRL+C
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrl')

    #volta p/ pag do ponto
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #prox campo
    pyautogui.press(['tab'])

    #CTRL+V
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrl')

    #volta p/ excel
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #Vai p/ hora do almoço
    pyautogui.press(['tab'])

    #CTRL+C
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrl')

    #volta p/ pag do ponto
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #prox campo
    pyautogui.press(['tab'])

    #CTRL+V
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrl')

    #vai apra o confirmar
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
    pyautogui.press(['enter'])

    time.sleep(2)

    #Clicar em add
    buttonAdd = pyautogui.locateOnScreen('AddButton.png')
    pyautogui.click(buttonAdd)

    #Aguardar 1seg
    time.sleep(1)

    #volta p/ excel
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #Vai p/ data
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab'])

    #CTRL+C p/ data
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrl')

    #volta p/ pag ponto
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #CTRL+v p/ data
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrl')

    #volta p/ excel
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #vai para celula da hora de retorno do almoço
    pyautogui.press(['left', 'left', 'left', 'left', 'left'])

    #CTRL+C
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrl')

    #volta p/ pag do ponto
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #prox campo
    pyautogui.press(['tab'])

    #CTRL+V
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrl')

    #volta p/ excel
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #Vai p/ hora do final
    pyautogui.press(['tab'])

    #CTRL+C
    pyautogui.keyDown('ctrl')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrl')

    #volta p/ pag do ponto
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #prox campo
    pyautogui.press(['tab'])

    #CTRL+V
    pyautogui.keyDown('ctrl')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrl')

    #vai apra o confirmar
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab'])
    pyautogui.press(['enter'])

    #volta p/ excel
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    #prox data
    pyautogui.press(['right', 'right', 'right', 'right'])
    pyautogui.press(['down'])

