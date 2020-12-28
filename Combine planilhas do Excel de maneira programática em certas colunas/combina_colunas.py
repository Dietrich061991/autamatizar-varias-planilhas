# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:36:11 2020

@author: Dietrich
@careers: specialist in machine learning
@linkedin : https://www.linkedin.com/in/dietrich-montcho-b13672121/

"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd     #biblioteca para analise de dados
import glob             #biblioteca para chamar os arquivos em um diretorio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#entrar no diretorio onde estão armazenados os arquivos que iremos precisar 
diretorio = r'C:\Users\sdietrich\Documents\Data science project\script python automação\Combine planilhas do Excel de maneira programática em certas colunas'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#pegando todos os arquivos com o formato .xlsx no diretorio 
arquivos = glob.glob(diretorio + "/*.xlsx")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#pegando nos arquivos as colunas que queremos concaterna em um unico arquivo (neste caso queremos concartenar as colunas "Pais" e "venda")
colunas_desejadas = ["Pais","venda"]
df_total = pd.DataFrame(columns=colunas_desejadas)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Para cada arquivo no diretorio 
for arquivo in arquivos:
    # leia arquivo
    df_arquivos = pd.read_excel(arquivo)
    #printa os arquivos
    print(df_arquivos,'\n')
    #pegar somente os dados nas colunas "Pais","venda" 
    colunas_selecionadas = df_arquivos.loc[:, colunas_desejadas]
    #printar colunas selecionadas
    print(colunas_selecionadas)
    #juntando os dados das colunas "Pais","venda" em cada arquivo 
    df_total = pd.concat([colunas_selecionadas, df_total], ignore_index=False)
    print(df_total)
    #gerando a saida no formato xlsx
    df_total.to_excel("venda_geral.xlsx")

###########################################################################################################################################################################