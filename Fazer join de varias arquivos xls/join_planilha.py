# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:36:11 2020

@author: Dietrich
@careers: specialist in machine learning
@linkedin : https://www.linkedin.com/in/dietrich-montcho-b13672121/
"""
########################################################################################################################################################################################################
#biblioteca para fazer analise de dados

import pandas as pd
#bibliteca que lida com a geraçao de arquivo de saida 
from openpyxl.workbook import Workbook

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#pegando os arquivos que iremos usar no diretorio
planilha1 = (r'C:\Users\sdietrich\Documents\Data science project\script python automação\Fazer join de varias arquivos xls\Planilha1.xlsx')
planilha2 = (r'C:\Users\sdietrich\Documents\Data science project\script python automação\Fazer join de varias arquivos xls\Planilha2.xlsx')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lendo os arquivos 
df1_planilha1 = pd.read_excel(planilha1)
df2_planilha2 = pd.read_excel(planilha2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#armazenando as colunas de cada datframe em uma lista
colunas_df1_planilha1 = df1_planilha1.columns.values.tolist()
colunas_df2_planilha2 = df2_planilha2.columns.values.tolist()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#vamos percorer as duas colunas(colunas_df1_planilha1 e colunas_df2_planilha2) e retorna uma una lista onde as colunas estão iguais
colunas_final_join = [x for x in colunas_df1_planilha1 if x in colunas_df2_planilha2]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# criando dois novo dataFrame com usanda os dataframe anteriores e definidos as novas colunas em comum que criamos anterioramente
new_df1_planilha1 = df1_planilha1[colunas_final_join]
new_df2_planilha2 = df2_planilha2[colunas_final_join]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# concatenado os dois dataframes
join = [new_df1_planilha1, new_df2_planilha2]
join_planilhas = pd.concat(join)
print(join_planilhas)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#gerando uma saida do arquivo relatorio.xlsx no formato excel no diretorio especifico 
join_planilhas.to_excel(r'C:\Users\sdietrich\Documents\Data science project\script python automação\Fazer join de varias arquivos xls\relatorio.xlsx',sheet_name='Join_campos_iguais_1', index=False)
        
############################################################################################################################################################################################################