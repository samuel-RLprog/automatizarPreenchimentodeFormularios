import pyautogui
import time
import pandas as pd


#Acessar planilha
contatos = pd.read_csv('contatos.csv', sep=',')

#da uma pausa entre a execução do paytogui
pyautogui.PAUSE = 0.5
# Abrir navegador
pyautogui.press('win')
# Selecionar o navegaro
pyautogui.write('chrome')
#carregar o navegador
pyautogui.press('enter')
#acessar o site
pyautogui.write('file:///C:/Automacao/form.html')
#acessar o site
pyautogui.press('enter')    

try:
    # Esperar o site carregar
    time.sleep(5)

    for linha in contatos.index:
        time.sleep(1)
        pyautogui.click(x=3409, y=265)
        pyautogui.write(contatos['nome'][linha])
        pyautogui.press('tab')
        pyautogui.write(contatos['email'][linha])
        pyautogui.press('tab')  
        pyautogui.write(contatos['telefone'][linha])
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(x=3409, y=265)
except ValueError:
    print("Erro ao preencher o formulário. Verifique os dados na planilha.")  
    










