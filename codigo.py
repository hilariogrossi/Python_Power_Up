# Importar Bibliotecas em Python
# RPA - Automação de Processos por Robos
import pyautogui
import time
import pandas

# Passo a passo do projeto
# Passo 1 - Entar no sistema da empresa
## https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 1

pyautogui.hotkey('Super', 'A')

pyautogui.press('chrome')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

pyautogui.press('enter')

time.sleep(5)

# Passo 2 - Fazer login
pyautogui.click(x=2660, y=494) # x=1752, y=209
pyautogui.write('hilariogrossi') # login

pyautogui.press('tab')

pyautogui.write('123') # senha

pyautogui.click(x=1751, y=440)

time.sleep(3)

# Passo 3 - Importar a base de dados
tabela = pandas.read_csv('/home/hilario/Hashtag_Programacao/Python_Power_Up/produtos.csv')
print(tabela)

# Passo 4 - Cadastrar um produto
# pyautogui.click(x=1771, y=232)

# Passo 5 - Repetir isso até acabar a base de dados
for linha in tabela.index:
    pyautogui.click(x=1771, y=232)

    codigo = tabela.loc[linha, 'codigo']

    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']

    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)
