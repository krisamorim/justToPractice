from time import time
#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python
import pyautogui
import time
import os
os.chdir(r'C:\Users\Kris.Furtado\OneDrive - Deliver IT\Documentos\Code\justToPractice\Coder\Python\automationMouseKeyboad')


####################-->>>>> QUINTA <<<<<--####################
####Clicar no card de REPORT da QUINTA
pyautogui.click(x=921, y=412)
#aguarda
time.sleep(3)
#Clicar no menu dropdown
pyautogui.click(x=1119, y=673)
#aguardar 1 seg
time.sleep(1)
#Digitar apresentação
pyautogui.write('apresenta')
#aguardar
time.sleep(2)
#ir para botão update e dar enter
pyautogui.press(['enter', 'tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de DAILY da QUINTA
pyautogui.click(x=967, y=570)
time.sleep(2)
pyautogui.click(x=1125, y=674)
time.sleep(1)
pyautogui.write('reuni')
#aguardar
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de QUADRO KANBAN da QUINTA
#clicar no card
pyautogui.click(x=1013, y=675)
#aguardar 2 p/ card carregar
time.sleep(2)
#clicar no menu dropDão p/ selecionar tipo de atividade
pyautogui.click(x=1124, y=674)
#Aguardar menu carregar
time.sleep(2)
#digitar gest para buscar pela opção gestão
pyautogui.write('gest')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)

####Add Registro de Revisão do projeto na QUINTA
#clicar no vazio da coluna da quinta
pyautogui.click(x=962, y=969)
time.sleep(1)
#clicar no botão add tarefa
pyautogui.click(x=945, y=701)
time.sleep(2)
pyautogui.write('12404')
time.sleep(4)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab'])
pyautogui.write('Revisão do projeto')
pyautogui.press(['tab', 'tab', 'tab'])
time.sleep(1)
pyautogui.write('3,5')
pyautogui.press(['tab', 'tab'])
pyautogui.write('gest')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])

####Add Registro de Suporte ao time na QUINTA
#clicar no vazio da coluna da quinta
pyautogui.click(x=962, y=969)
time.sleep(1)
#clicar no botão add tarefa
pyautogui.click(x=941, y=807)
time.sleep(2)
pyautogui.write('12404')
time.sleep(4)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab'])
pyautogui.write('Suporte ao time e oneAnOne')
pyautogui.press(['tab', 'tab', 'tab'])
time.sleep(1)
pyautogui.write('3')
pyautogui.press(['tab', 'tab'])
pyautogui.write('gest')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])

time.sleep(2)

print("Segunda")
print("card: ",pyautogui.position())
time.sleep(5)
print("DroDown: ",pyautogui.position())
time.sleep(5)

print("\nTerça")
print("card: ",pyautogui.position())
time.sleep(5)
print("DroDown: ",pyautogui.position())
time.sleep(5)

print("\Quarta")
print("card: ",pyautogui.position())
time.sleep(5)
print("DroDown: ",pyautogui.position())
time.sleep(5)

print("\Quinta")
print("card: ",pyautogui.position())
time.sleep(5)
print("DroDown: ",pyautogui.position())
time.sleep(5)

print("\Sexta")
print("card: ",pyautogui.position())
time.sleep(5)
print("DroDown: ",pyautogui.position())