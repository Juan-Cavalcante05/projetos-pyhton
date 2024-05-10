# codigo para mandar relatorio de vendas para email da empresa(automatizado)
import pyautogui
import pyperclip
import time
# escrever o passa a passo
# passo 1 - entrar no sistema da empresa(nesse caso é o drive)
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(3)

# passo 2 - navegar no sistema até encontrar a base de dados
pyautogui.click(x=350, y=269, clicks=3)
time.sleep(2)

# passo 3 - exportar a base de vendas
pyautogui.click(x=404, y=426)
pyautogui.click(x=1164, y=161)
pyautogui.click(x=956, y=566)
time.sleep(5)

#https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

# passo 4 - caucular os indicadores(faturamento e quantidade de produtos vendidos
# pandas, numpy e openpyxl
import pandas as pd
import numpy
import openpyxl
tabela = pd.read_excel(r'C:\Users\juanc\Downloads\Vendas - Dez.xlsx') #sheets = posição da aba ou o nome dela
display(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(faturamento)
print(quantidade)


# passo 5 - enviar email para o diretorio com os indicadores
pyautogui.hotkey('ctrl','t') # abrir nova aba
pyperclip.copy('https://mail.google.com/mail?hl=pt-BR') # link copiado
pyautogui.hotkey('ctrl','v') # colei o link
pyautogui.press('enter') # entrar no site
time.sleep(5)

# clicar no btão escrever
pyautogui.click(x=84, y=164)
time.sleep(2)
# escrerver destinatario(quem vai receber o email)
pyautogui.write('sandymaria3377@gmail.com')
pyautogui.press('tab')
# escrever assunto
pyautogui.press('tab')# pular para o campo do assunto
pyautogui.write('teste do intensivão. te amo')

# escrever o corpo de email
pyautogui.press('tab') # pular para campo de escrever email
texto=f'''Esse é test do codigo que eu fiz
o computador ta fazendo tudo sozinho, ate esse email, foi ele que escreveu.
R$ {faturamento:,.2f}
a quantidade de produtos foi:{quantidade:,}'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
# anexar arquivos
pyautogui.click(x=960, y=688)
pyautogui.click(x=447, y=353, clicks=2)
# enviar email
time.sleep(5)
pyautogui.hotkey('ctrl','enter')


time.sleep(5)
pyautogui.position()


