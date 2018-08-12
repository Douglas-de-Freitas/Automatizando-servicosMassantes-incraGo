'''
# Python 3 code
import urllib.request, urllib.parse, urllib.error
 
url = 'http://sipra.incra.gov.br/Beneficiario/Relatorios/benef_espelho.asp?c_beneficiario_identificacao_codigo=go039000000033'
 
print("baixando com urllib")
urllib.request.urlretrieve(url, "o-fantasma-da-opera-u.png")
'''

#print(aqv.readline(14))
#webbrowser.open(url, new=0, autoraise=True)

import webbrowser
import time
import pyautogui

url = ('http://sipra.incra.gov.br/Beneficiario/Relatorios/benef_espelho.asp?c_beneficiario_identificacao_codigo=')
aqv = open('arquivo.txt', 'r')
complemento = ''

for line in aqv:
    complemento = url + line
    webbrowser.open(complemento, new=0, autoraise=True)
    time.sleep(20)
    pyautogui.hotkey("ctrl", "p") # pressiona a combinação "Control + P" imprimi tela atual
    time.sleep(4)
    pyautogui.press("enter")     # simula o pressionamento da tecla enter para imprimir
    time.sleep(1)
    pyautogui.hotkey("ctrl", "w") # pressiona a combinação "Control + W" fecha a aba atual do navegador
    




