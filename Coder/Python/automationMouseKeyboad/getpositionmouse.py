from time import time
#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python
import pyautogui
import time
import os
os.chdir(r'C:\Users\Kris.Furtado\OneDrive - Deliver IT\Documentos\Code\justToPractice\Python\automationMouseKeyboad')


time.sleep(2)
#buttonProx = pyautogui.locateOnScreen('proxPage.png')
#pyautogui.click(buttonProx)


print(pyautogui.position())