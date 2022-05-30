from time import time
#se o pyautgui não funcionar para reconhcer a imagem AddButton.png execute esse comendo no terminal pip install opencv-python
import pyautogui
import time


'''
<-- ATENÇÃO -->
1-Dependendo do OS or arquivo deve ser alterado de CRLF (Windows) para LF (Unic/MAC)
2-Definir o lop na linha 124  (Ler comentario da linha)                    
3-O excel não pode ter espaço vasion entre as linhas e as datas devem vicar 3 coluna após a hora de saida (confira na linha 39 quantos lefts são feitos da data para o horario inicial)
4-antes de inicicar deixe a data inicial selecionada no excel e a pagina deo alt+tab pronta no background, para que o alt+tab entre excel e navegador funcione
5-Seria bom rodar pit install Pillow autogui 
'''
############### CRIANDO FUNÇÕES ####################################

def botaAdd_Cantosuperior():
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
    time.sleep(2)

def botaAdd_Cantosuperior2():
    pyautogui.click(x=1899, y=207)
    time.sleep(2)
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
    time.sleep(2)

def alternar():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

def copiar():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

def colar():
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

def copiar_cel_horaInicio():
    #vai para celura da hora do inicio do expediente
    pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left', 'left'])
    copiar()
    time.sleep(1)

def copiar_campo_Adjacente():
    pyautogui.press('tab')
    copiar()
    time.sleep(1)

def salvar_turno():
    pyautogui.press(['tab', 'tab', 'tab', 'enter'])
    time.sleep(1)

def primeiro_turno():
    # Copiar data do excel
    copiar()
    # ir para navegador
    alternar()
    # enter no botão superior add
    botaAdd_Cantosuperior()

    colar()
    # voltar para o excel para pegar data novamente
    alternar()

    copiar_cel_horaInicio()
    # volta para o navegador
    alternar()
    # proximo campo
    pyautogui.press('tab')

    colar()
    # volta para o excel para pegar a hora de saida p/ o almoço
    alternar()

    copiar_campo_Adjacente()
    # volta para o navegador
    alternar()
    # salta para o proximo campo
    pyautogui.press('tab')

    colar()
    pyautogui.press('tab')
    time.sleep(1)
    salvar_turno()

def segundo_turno():
    #volta para o excel
    alternar()
    #copiar adjacente
    copiar_campo_Adjacente()
    #Volta para o navag
    alternar()
    #clica no botão add
    botaAdd_Cantosuperior2()
    #Sai da data
    pyautogui.press('tab')
    #Cola hora do retorno do almoço
    colar()
    #Volta para o excel
    alternar()
    #Copia a celula adjacente
    copiar_campo_Adjacente()
    #volta para o navega(hora final)
    alternar()
    #vai para o campo da hora final
    pyautogui.press(['tab'])
    #cola a hora final
    colar()
    #Prox campo
    pyautogui.press('tab')
    time.sleep(1)
    salvar_turno()

def prox_linha():
    pyautogui.click(x=1899, y=207)
    alternar()
    pyautogui.press(['right', 'right', 'right', 'right', 'down'])

####################### EXECUÇÃO ###################################

#aguardar
time.sleep(10)
#Se tiver 30 linhas no excel coloque 29, se tive 20 coloque 19 e assim por diante, sempre uma  menos
qntids_desejadas = 20
for c in range(1,qntids_desejadas):
    primeiro_turno()
    segundo_turno()
    prox_linha()
    print('{} ja foi faltam {}'.format(c,qntids_desejadas-c))
