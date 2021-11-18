from sqlalchemy import create_engine
import random
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pandas as pd

################################################################################################################
# funcao que conecta meu codigo python com o sql
def conexao_sql():

    # parametros da conexao
    servidor = 'DESKTOP-46BRE9F\SQLEXPRESS'
    base = 'master'
    driver = 'ODBC Driver 17 for SQL Server'
    conexao = f'mssql://@{servidor}/{base}?driver={driver}'

    return create_engine(conexao)
################################################################################################################
def main():

    # configurar / setar as informacoes iniciais do meu pdf
    margem = 2
    pular_linha = Spacer(0.001*cm,0.2*cm)

    # criando o meu documento e setando as margens
    documento = SimpleDocTemplate(
                                    "Prova da Live 18.pdf"
                                    ,rightMargin    = margem*cm
                                    ,leftMargin     = margem*cm
                                    ,topMargin      = margem*cm
                                    ,bottomMargin   = margem*cm
                                 )

    # estilo do pdf
    estilo = getSampleStyleSheet()

    # criar a conexao
    engine = conexao_sql()

    # criar a lista que contem todas as perguntas e respostas da minha prova
    prova = []

    # cabecalho da prova
    cabecalho = [
                 "Prova da Live 18",
                 "Data:   __/__/__",
                 "Nome:   ____________________________________________"
                ]

    for i in cabecalho:
        prova.append(Paragraph(i, estilo["Normal"]))
        prova.append(pular_linha)
    prova.append(pular_linha)
    prova.append(pular_linha)

    # comecar a selecionar as perguntas e respostas
    qntd_perguntas = 1
    perguntas_sorteadas = []
    while qntd_perguntas <= 3:

        # escolher a pergunta de forma randomica
        pergunta_ja_foi = False
        sorteio_pergunta = random.randint(1,5)
        # verifica se o numero sorteado ja foi sorteado antes
        # caso ja foi sorteado, usa outro numero
        for numero in perguntas_sorteadas:
            if numero == sorteio_pergunta:
                pergunta_ja_foi = True
                break

        if pergunta_ja_foi == False:
            # incluindo a pergunta sortoeada na minha lista de verificacao
            perguntas_sorteadas.append(sorteio_pergunta)

            # query da pergunta
            requisicao_pergunta = f"""
                                        SELECT TOP 1 PERGUNTA
                                        FROM TB_PERGUNTAS
                                        WHERE CODIGO_PERGUNTA = {sorteio_pergunta}
                                    """

            perguntas = engine.execute(requisicao_pergunta)
            for i in perguntas:
                prova.append(Paragraph(f"{qntd_perguntas}) {i['PERGUNTA']}", estilo["Normal"]))
            prova.append(pular_linha)

            # adicionar as possiveis respostas referente a minha pergunta sorteada
            lista_respostas = []

            #  criei as queries
            requisicao_resposta_correta = f"""
                                                SELECT RESPOSTA
                                                FROM TB_RESPOSTAS
                                                WHERE CODIGO_PERGUNTA = {sorteio_pergunta}
                                                AND CORRECAO = 1
                                           """
            
            requisicao_resposta_incorreta = f"""
                                                SELECT TOP 4 RESPOSTA
                                                FROM TB_RESPOSTAS
                                                WHERE CODIGO_PERGUNTA = {sorteio_pergunta}
                                                AND CORRECAO <> 1
                                                ORDER BY NEWID()
                                             """

            # chamando as queries
            respostas_corretas = engine.execute(requisicao_resposta_correta)
            for i in respostas_corretas:
                lista_respostas.append(i['RESPOSTA'])

            respostas_incorretas = engine.execute(requisicao_resposta_incorreta)
            for i in respostas_incorretas:
                lista_respostas.append(i['RESPOSTA'])

            # embaralhar as respostas
            random.shuffle(lista_respostas)

            # adicionar as respostas na minha prova
            prova.append(Paragraph(f"a) {lista_respostas[0]}", estilo["Normal"]))
            prova.append(pular_linha)
            prova.append(Paragraph(f"b) {lista_respostas[1]}", estilo["Normal"]))
            prova.append(pular_linha)
            prova.append(Paragraph(f"c) {lista_respostas[2]}", estilo["Normal"]))
            prova.append(pular_linha)
            prova.append(Paragraph(f"d) {lista_respostas[3]}", estilo["Normal"]))
            prova.append(pular_linha)
            prova.append(Paragraph(f"e) {lista_respostas[4]}", estilo["Normal"]))

            # pulo algumas linhas para proxima pergunta
            prova.append(pular_linha)
            prova.append(pular_linha)

            # iteracao
            qntd_perguntas += 1

    # adiciono a prova no meu documento de pdf
    documento.build(prova)
################################################################################################################
main()


