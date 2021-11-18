import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

################################################################################################################################################################################################
#                _                                     _ _             
#  _ __ __ _ ___| |_ _ __ ___  __ _ _ __  ___ ___   __| (_) __ _  ___  
# | '__/ _` / __| __| '__/ _ \/ _` | '__|/ __/ _ \ / _` | |/ _` |/ _ \ 
# | | | (_| \__ \ |_| | |  __/ (_| | |  | (_| (_) | (_| | | (_| | (_) |
# |_|  \__,_|___/\__|_|  \___|\__,_|_|___\___\___/ \__,_|_|\__, |\___/ 
#                                   |_____|                |___/       
# Funcao responsavel por acessar o site dos correios e buscar a ultima atualizacao do seu pedido, a partir do codigo de rastreio
################################################################################################################################################################################################
def rastrear_codigo(codigo):
    
    # indico onde esta o meu executavel do chrome driver
    driver = webdriver.Chrome(r'D:\Programa 1-1\Lives\Live #020 - Web Scrapping nos Correios\chromedriver.exe')

    # obter o site dos correios
    driver.get("https://www2.correios.com.br/sistemas/rastreamento/default.cfm")
    time.sleep(2)

    # procurar a barra de pesquisa dos correios
    barra_pesquisa = driver.find_element_by_xpath('//*[@id="objetos"]')

    # limpar qlqr sujeira na barra de pesquisa
    barra_pesquisa.clear()
    barra_pesquisa.send_keys(codigo)

    # procurar o botao de buscar
    botao_buscar = driver.find_element_by_xpath('//*[@id="btnPesq"]')
    botao_buscar.click()

    # tempo para carregar o site dos correios com o resultado
    time.sleep(2)

    # procurar os elementos que contem a informacao desejada
    resultado = pd.DataFrame(driver.find_elements_by_tag_name('td'))
    n=0
    while n <= 11:
        print('\n')
        print(resultado[0][n].text)
        n += 1
    
    time.sleep(10)

    # fechar o chrome o driver
    driver.close()

################################################################################################################################################################################################
# ███    ███  █████  ██ ███    ██ 
# ████  ████ ██   ██ ██ ████   ██ 
# ██ ████ ██ ███████ ██ ██ ██  ██ 
# ██  ██  ██ ██   ██ ██ ██  ██ ██ 
# ██      ██ ██   ██ ██ ██   ████ 
#                                 
# Funcao responsavel por abrir o excel, obter os dados das mensagem e chamar as outras funcoes
################################################################################################################################################################################################
def main():

    # PY253390246BR
    # perguntar para o usuario qual seria o codigo de rastreio
    codigo = str(input('Por favor, insira o código de rastreio dos correios: '))

    # chamada da funcao que inicia o web scrapping
    rastrear_codigo(codigo)

################################################################################################################################################################################################

# chamada da funcao principal
main()



