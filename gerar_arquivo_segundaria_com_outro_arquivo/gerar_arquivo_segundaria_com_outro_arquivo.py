# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:36:11 2020

@author: Dietrich
@careers: specialist in machine learning
@linkedin : https://www.linkedin.com/in/dietrich-montcho-b13672121/

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#criar o arquivo hqls.txt 
#criar o arquivo hqls.txt
with open(r"C:\Users\sdietrich\Documents\Data science project\script python automação\gerar_arquivo_segundaria_com_outro_arquivo\hqls.txt", 'w') as fileHql:
    #ler o arquivo tabela.txt
    with open(r"C:\Users\sdietrich\Documents\Data science project\script python automação\gerar_arquivo_segundaria_com_outro_arquivo\tabela.txt" , 'r') as fileTabelas:
        listaTabelas = fileTabelas.readlines()
        listaTabelas = [tabela[0:-1] for tabela in listaTabelas]
        for tabela in listaTabelas:
            fileHql.write('ALTER TABLE P_BIGD_LZARNG_DB.' + tabela + ' DROP PARTITION (DT_FOTO > 1);')
            fileHql.write('\n') 

###############################################################################################################################################################################
           