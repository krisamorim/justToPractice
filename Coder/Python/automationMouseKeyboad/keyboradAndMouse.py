import time, pyautogui


time.sleep(2)
pyautogui.click(x=60, y=17)
time.sleep(2)
pyautogui.click(x=828, y=990)
pyautogui.write('Mapeamento e registroooooooooooooooooooooooooooooooo')

tempoEspera = 90
for c in range(1,42):
    time.sleep(tempoEspera)
    pyautogui.press('backspace')
    time.sleep(tempoEspera)
    pyautogui.moveTo(x=1820, y=421)
    time.sleep(tempoEspera)
    pyautogui.click(x=1535, y=993)