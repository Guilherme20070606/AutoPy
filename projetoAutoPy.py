# passo 1: entrar no sistema da empresa
# passo 2: fazer login
# passo 3: abrir a base de dados da empresa
# passo 4: cadastrar um produto
# passo 5: repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# passo 1: entrar no sistema da empresa 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
time.sleep(2.5)
pyautogui.press("enter")

# pausa maior para carregar o site
time.sleep(2)

# passo 2: fazer login
pyautogui.click(x=599, y=374)
pyautogui.write("guialmeidabjj7@gmail.com")
pyautogui.press("tab")
pyautogui.write("6814005274")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

# clicar para abrir a área de cadastro
pyautogui.click(x=700, y=266)

# passo 3: abrir a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# passo 4 e 5: cadastrar produtos
for Linha in tabela.index:

    pyautogui.click(x=435, y=259)

    codigo = str(tabela.loc[Linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[Linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[Linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[Linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[Linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[Linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = tabela.loc[Linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
