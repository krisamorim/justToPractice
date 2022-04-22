for i in range(5):
    print("a"*i)


time.sleep(3)

#add analise de tarefas 6h na segunda
#mover o mouse para baixo
pyautogui.click(x=359, y=804)
#clicar no botão +
addJira = pyautogui.locateOnScreen('addJira.png')
pyautogui.click(addJira)