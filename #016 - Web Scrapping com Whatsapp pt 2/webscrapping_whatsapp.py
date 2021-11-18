import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

################################################################################################################################################################################################
# ███████ ███    ██ ██    ██ ██  █████  ██████          ███    ███ ███████  ██████  
# ██      ████   ██ ██    ██ ██ ██   ██ ██   ██         ████  ████ ██      ██       
# █████   ██ ██  ██ ██    ██ ██ ███████ ██████          ██ ████ ██ ███████ ██   ███ 
# ██      ██  ██ ██  ██  ██  ██ ██   ██ ██   ██         ██  ██  ██      ██ ██    ██ 
# ███████ ██   ████   ████   ██ ██   ██ ██   ██ ███████ ██      ██ ███████  ██████  
#
# Funcao responsavel encontrat a barra de texto, digitar o texto, e clicar em enviar
################################################################################################################################################################################################
def enviar_msg(msg, driver):

    # procuro a barra de texto do wpp web e digito texto
    barra_msg = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    barra_msg.send_keys(msg)

    # procuro o bota de enviar msg e clico
    botao_enviar = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    botao_enviar.click()

    # esperar um pouco
    time.sleep(2)

################################################################################################################################################################################################
# ██████  ██    ██ ███████  ██████  █████  ██████           ██████  ██████  ███    ██ ████████  █████  ████████  ██████          ██     ██ ██████  ██████  
# ██   ██ ██    ██ ██      ██      ██   ██ ██   ██         ██      ██    ██ ████   ██    ██    ██   ██    ██    ██    ██         ██     ██ ██   ██ ██   ██ 
# ██████  ██    ██ ███████ ██      ███████ ██████          ██      ██    ██ ██ ██  ██    ██    ███████    ██    ██    ██         ██  █  ██ ██████  ██████  
# ██   ██ ██    ██      ██ ██      ██   ██ ██   ██         ██      ██    ██ ██  ██ ██    ██    ██   ██    ██    ██    ██         ██ ███ ██ ██      ██      
# ██████   ██████  ███████  ██████ ██   ██ ██   ██ ███████  ██████  ██████  ██   ████    ██    ██   ██    ██     ██████  ███████  ███ ███  ██      ██      
#
# Funcao responsavel por buscar os contatos no wpp web, e chamar a funcao que enviar a msg
################################################################################################################################################################################################
def buscar_contato_wpp(lista_msg_excel):
    
    # indico onde esta o meu executavel do chrome driver
    driver = webdriver.Chrome('D:\\Programa 1-1\\Lives\\Live #016 - Web Scrapping com Whatsapp pt 2\\chromedriver.exe')

    # obter o site do wpp web
    driver.get("https://web.whatsapp.com/")

    # gatilho para continuar a executar o codigo depois que eu apertar enter
    print('\n\nAperte o Enter para continuar\n\n')
    input()

    # procurar a barra de pesquisa de contatos do wpp
    barra_pesquisa = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

    # rodar todos os contatos da lista e enviar as msgs para cada um deles
    for index, contato_excel in lista_msg_excel.iterrows():

        # limpar qlqr sujeira na barra de pesquisa
        barra_pesquisa.clear()
        barra_pesquisa.send_keys(contato_excel[0])
        time.sleep(4)

        # obter a lista de contato encontrados depois pesquisa
        lista_contatos_wpp = driver.find_elements_by_class_name('_3Pwfx')

        # rodar todos contatos da lista e se eu encontrar o msm nome que busco, enviar msg
        for contato_wpp in lista_contatos_wpp:

            # comparar se é o mesmo nome de contato que esta no excel
            if contato_wpp.text.split('\n')[0] == contato_excel[0]:
                
                contato_wpp.click()

                # msg de bom dia
                msg_inicial = "Bom dia, " + contato_excel[0] + ", tudo bem com você?"
                enviar_msg(msg_inicial, driver)

                # msg do excel
                enviar_msg(contato_excel[1], driver)
    
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

    # nomes das colunas do excel
    col_nome = 'Nome'
    col_mensagem = 'Mensagem'

    # leitura das informacoes contidas no excel
    info_excel = pd.read_excel('D:\\Programa 1-1\\Lives\\Live #016 - Web Scrapping com Whatsapp pt 2\\Anexos\\msg_wpp.xlsx')

    # criar lista/matriz que contem as duas colunas com informacoes do excel
    lista_msg_excel = (info_excel[[col_nome,col_mensagem]])

    # uso um dataframe do pandas para eliminar sujeiras na minha tabela
    df_lista_msg_excel = pd.DataFrame(lista_msg_excel)
    df_lista_msg_excel = df_lista_msg_excel.dropna()

    # chamada da funcao que inicia o web scrapping
    buscar_contato_wpp(df_lista_msg_excel)

################################################################################################################################################################################################

# chamada da funcao principal
main()