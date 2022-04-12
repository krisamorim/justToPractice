from time import time
#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python
import pyautogui
import time
import os
os.chdir(r'C:\Users\Kris.Furtado\OneDrive - Deliver IT\Documentos\Code\justToPractice\Coder\Python\automationMouseKeyboad')

time.sleep(10)

####################-->>>>> SEGUNDA <<<<<--####################
####Clicar no card de REPORT da SEGUNDA
pyautogui.click(x=387, y=421)
#aguarda
time.sleep(3)
#Clicar no menu dropdown
pyautogui.click(x=1127, y=589)
#Digitar apresentação
pyautogui.write('apresenta')
#aguardar
time.sleep(2)
#ir para botão update e dar enter
pyautogui.press(['enter', 'tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de DAILY da SEGUNDA
pyautogui.click(x=361, y=566)
time.sleep(2)
pyautogui.click(x=1126, y=671)
time.sleep(1)
pyautogui.write('reuni')
#aguardar
time.sleep(2)
#ir para botão update e dar enter
pyautogui.press(['enter', 'tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de REVISÃO DE KANBAN da SEGUNDA
pyautogui.click(363, 678)
time.sleep(2)
pyautogui.click(x=1121, y=666)
time.sleep(2)
pyautogui.write('apresenta')
time.sleep(2)
pyautogui.press(['enter','tab', 'tab', 'enter'])

####################-->>>>> TERÇA <<<<<--####################
####Clicar no card de REPORT da TERÇA
pyautogui.click(x=572, y=420)
#aguarda
time.sleep(3)
#Clicar no menu dropdown
pyautogui.click(x=1124, y=669)
time.sleep(1)
#Digitar apresentação
pyautogui.write('apresenta')
#aguardar
time.sleep(2)
#ir para botão update e dar enter
pyautogui.press(['enter', 'tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de DAILY da TERÇA
pyautogui.click(x=545, y=586)
time.sleep(2)
pyautogui.click(x=1123, y=672)
time.sleep(1)
pyautogui.write('reuni')
#aguardar
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de QUADRO KANBAN da TERÇA
pyautogui.click(x=548, y=670)
time.sleep(2)
pyautogui.click(x=1120, y=671)
time.sleep(2)
pyautogui.write('gest')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)

####Add Registro de Duvidas da TERÇA
pyautogui.click(x=528, y=810)
time.sleep(2)
pyautogui.click(x=528,y=708)
time.sleep(2)
pyautogui.write('12404')
time.sleep(4)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab'])
pyautogui.write('Mapeamento e registro de duvidas')
pyautogui.press(['tab', 'tab', 'tab'])
time.sleep(1)
pyautogui.write('3')
pyautogui.press(['tab', 'tab'])
pyautogui.write('duvida su')
time.sleep(3)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])

####################-->>>>> QUARTA <<<<<--####################
####Clicar no card de REPORT da QUARTA
pyautogui.click(x=755, y=412)
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

####Clicar no card de DAILY da QUARTA
pyautogui.click(x=711, y=586)
time.sleep(2)
pyautogui.click(x=1123, y=672)
time.sleep(1)
pyautogui.write('reuni')
#aguardar
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de QUADRO KANBAN da QUARTA
#clicar no card
pyautogui.click(x=835, y=675)
#aguardar 2 p/ card carregar
time.sleep(2)
#clicar no menu dropDão p/ selecionar tipo de atividade
pyautogui.click(x=1124, y=670)
#Aguardar menu carregar
time.sleep(2)
#digitar gest para buscar pela opção gestão
pyautogui.write('gest')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)

####Add Registro de PLANO DE DEV da QUARTA
#clicar no vazio da coluna da quarta
pyautogui.click(x=724, y=864)
time.sleep(1)
#clicar no botão add tarefa
pyautogui.click(x=738, y=693)
time.sleep(2)
pyautogui.write('12404')
time.sleep(4)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab'])
pyautogui.write('Mapeamento/revisão e definição de execução de sequencia de dev')
pyautogui.press(['tab', 'tab', 'tab'])
time.sleep(1)
pyautogui.write('3')
pyautogui.press(['tab', 'tab'])
pyautogui.write('gest')
time.sleep(3)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])

####Add Registro de MAPEAMENTO DE DUVIDAS da QUARTA
#clicar no vazio da coluna da quarta
pyautogui.click(x=771, y=968)
time.sleep(1)
#clicar no botão add tarefa
pyautogui.click(x=742, y=797)
time.sleep(2)
pyautogui.write('12404')
time.sleep(4)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab'])
pyautogui.write('Mapeamento de duvidas')
pyautogui.press(['tab', 'tab', 'tab'])
time.sleep(1)
pyautogui.write('3,5')
pyautogui.press(['tab', 'tab'])
pyautogui.write('duvida s')
time.sleep(3)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])


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

####################-->>>>> SEXTA <<<<<--####################
####Clicar no card de REPORT da SEXTA
pyautogui.click(x=1172, y=409)
#aguarda
time.sleep(3)
#Clicar no menu dropdown
pyautogui.click(x=1120, y=671)
#aguardar 1 seg
time.sleep(1)
#Digitar apresentação
pyautogui.write('apresenta')
#aguardar
time.sleep(2)
#ir para botão update e dar enter
pyautogui.press(['enter', 'tab', 'tab', 'enter'])
time.sleep(2)

####Clicar no card de DAILY da SEXTA
pyautogui.click(x=1162, y=568)
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

####Clicar no card de QUADRO KANBAN da SEXTA
#clicar no card
pyautogui.click(x=1155, y=660)
#aguardar 2 p/ card carregar
time.sleep(2)
#clicar no menu dropDão p/ selecionar tipo de atividade
pyautogui.click(x=1122, y=664)
#Aguardar menu carregar
time.sleep(2)
#digitar gest para buscar pela opção gestão
pyautogui.write('gest')
time.sleep(2)
pyautogui.press(['enter'])
time.sleep(1)
pyautogui.press(['tab', 'tab', 'enter'])
time.sleep(2)


#proxima pagina
buttonProx = pyautogui.locateOnScreen('proxPage.png')
pyautogui.click(buttonProx)

# pyautogui.write('Digite seu texto aqui')
#pyautogui.move()

#mover mouse p/ uma posição especifica
#pyautogui.moveTo()

#Arrastar
#pyautogui.drag()