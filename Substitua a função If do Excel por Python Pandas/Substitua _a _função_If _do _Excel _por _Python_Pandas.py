import numpy as np
import pandas as pd

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lendo o arquivo Teste.xlxs
Teste_df = pd.read_excel(r'C:\Users\sdietrich\Documents\Data science project\script python automação\Substitua a função If do Excel por Python Pandas\Teste.xlsx')
#print(Teste_df)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#criando a coluna media_teste onde iremos armazenar a media dos Testes realizadas por cada um
Teste_df['media_teste'] = Teste_df.mean(axis=1)
#print(Teste_df)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Testante if com funçao numpy
#criando uma nova coluna chamada Passa/Reprova onde será inserido 'Passa' quando a media for superior a 60 e'Reprova' quando inferior á 60 
#Teste_df['Passa/Reprova'] = np.where(Teste_df['media_teste'] > 60, 'Passa', 'Reprova')
#print(Teste_df)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#criando algumas condicoes que iremos u
conditions = [
(Teste_df['media_teste'] >= 90),
(Teste_df['media_teste'] < 90) & (Teste_df['media_teste'] >= 80),
(Teste_df['media_teste'] < 80) & (Teste_df['media_teste'] >= 70),
(Teste_df['media_teste'] < 70) & (Teste_df['media_teste'] >= 60),
(Teste_df['media_teste'] < 60)
]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#criando uma Lista chamada results onde cada elemento da lista representa uma condiçao definida acima 
'''
    'A'  representa a condiçao 1
    'B   representa a condiçao 2
    'C'  representa a condiçao 3
    'D   representa a condiçao 4
    'E'  representa a condiçao 5
    'F   representa a condiçao 6
     
'''
results = ['A', 'B', 'C', 'D', 'F']

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#criando uma nova coluna chamda Lettra onde iremos colocar cada lettra definida de acordo com a condiçao definidas com a media_tese
Teste_df['Lettra'] = np.select(conditions, results)
#print(Teste_df)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# testando if do Excel
Teste_df['Passa/Reprova'] = ['Passa' if x > 60 else 'Reprova' for x in Teste_df['media_teste']]
print(Teste_df)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Teste_df.to_excel(r'C:\Users\sdietrich\Documents\Data science project\script python automação\Substitua a função If do Excel por Python Pandas\Relatorio_teste.xlsx', index=False, sheet_name='Relatorio')
