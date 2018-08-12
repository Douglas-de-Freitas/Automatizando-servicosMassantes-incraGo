'''
# Python 3 code
import urllib.request, urllib.parse, urllib.error
 
url = 'http://sipra.incra.gov.br/Beneficiario/Relatorios/benef_espelho.asp?c_beneficiario_identificacao_codigo=go039000000033'
 
print("baixando com urllib")
urllib.request.urlretrieve(url, "o-fantasma-da-opera-u.png")
'''

#print(aqv.readline(14))
#webbrowser.open(url, new=0, autoraise=True)
import clipboard # clipboard.copy(data)
import webbrowser
import time
import pyautogui

url = ('http://sipra.incra.gov.br/beneficiario/Relatorios/Relatorio_relacao_de_beneficiarios_totalI.asp?cod=')
aqv = open('arquivo.txt', 'r')
complemento = ''

contador = 1

for line in aqv:
	complemento = url + line
	webbrowser.open(complemento, new=0, autoraise=True)
	time.sleep(6)
	pyautogui.hotkey("ctrl", "p")
	time.sleep(4)
	pyautogui.press("enter")
	time.sleep(2)
	clipboard.copy(str(line).rstrip('\n'))
	time.sleep(0.5)
	pyautogui.hotkey("ctrl", "v")
	time.sleep(1.5)
	pyautogui.press("enter")
	time.sleep(1.5)
	pyautogui.hotkey("ctrl", "w")
	time.sleep(1.5)
	contador = contador + 1
