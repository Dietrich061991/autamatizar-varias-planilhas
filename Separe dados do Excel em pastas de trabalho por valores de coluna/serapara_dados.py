# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:36:11 2020

@author: Dietrich
@careers: specialist in machine learning
@linkedin : https://www.linkedin.com/in/dietrich-montcho-b13672121/
"""


########################################################################################################################################################################################################
#biblioteca para fazer manipulação de dados
import pandas as pd 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lendo o arquivo Venda.xlxs
df_venda = pd.read_excel(r'C:\Users\sdietrich\Documents\Data science project\script python automação\Separe dados do Excel em pastas de trabalho por valores de coluna\venda.xlsx')
print(df_venda)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#pegando os valores unicos na coluna Frutas
valor_unica = df_venda['Frutas'].unique()
print(valor_unica)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Gerando os arquivos de saida com o tipo de frutas (cada arquivo armazenará somente uma Fruta)
for value in valor_unica:
    df_venda1 = df_venda[df_venda['Frutas'] == value]
    saida_arquivos = "Fruta_" + str(value) + ".csv"
    df_venda1.to_csv(saida_arquivos , index=False)

########################################################################################################################################################################################################
