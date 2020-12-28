
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:36:11 2020

@author: Dietrich
@careers: specialist in machine learning
@linkedin : https://www.linkedin.com/in/dietrich-montcho-b13672121/
"""

#-----------------------------------------------------------------------------------------------------------------------------
#Este pacote é para ler dados e formatar informações de arquivos Excel 
import xlrd

#-----------------------------------------------------------------------------------------------------------------------------
#pegando os arquivos que iremos usar no diretorio
planilha1 = (r'C:\Users\sdietrich\Documents\Data science project\script python automação\autamatizar varias planilhas\Planilha1.xlsx')
planilha2 = (r'C:\Users\sdietrich\Documents\Data science project\script python automação\autamatizar varias planilhas\Planilha2.xlsx')

#-----------------------------------------------------------------------------------------------------------------------------
#lendo cada arquivo
relatorio1 = xlrd.open_workbook(planilha1)

relatorio2 = xlrd.open_workbook(planilha2)
#-----------------------------------------------------------------------------------------------------------------------------
#pegue a primeira folha pelo índice  (as folhas são indexadas a zero)
Primeira_planilha = relatorio1.sheet_by_index(0)

#pegue a segunda folha pelo índice  (as folhas são indexadas a zero)
Segunda_planilha = relatorio2.sheet_by_index(0)

#-----------------------------------------------------------------------------------------------------------------------------
#printando o cabeçalho da planilha1(header)
cabecalho_planilha1 = Primeira_planilha.row_values(0)
print(f'Printando o cabecalho da planilha 1 ==================================> {cabecalho_planilha1}')

#selecionando a coluna que iremos usar(neste caso vamos usar a coluna que está na posição 1. basta você passar a posiçao da coluna que deseja.)
coluna = cabecalho_planilha1[1]
print(f'Printando a coluna que selecionamos na planilha 1 ====================> {coluna}')


#-----------------------------------------------------------------------------------------------------------------------------

i = 0
total = 0

for row in range(Primeira_planilha.nrows):
    if str(Primeira_planilha.cell(row,1).value) == "pizza":
        i = i +1
        total = total + (Primeira_planilha.cell(row,2).value)
    else:
        pass

for row in range(Segunda_planilha.nrows):
    if str(Segunda_planilha.cell(row,1).value) == "pizza":
        i = i +1
        total = total + (Segunda_planilha.cell(row,2).value)
    else:
        pass

print(f'Quantidade total de pizza que foi vendida nas duas planilhas =========> {i}')
print(f'Venda total das {i} pizza vendidas na duas planilhas ==================> {total}')
print(f'Valor media de Pizza vendida se baseando nas duas planilha ===========> {total/i}')

#-----------------------------------------------------------------------------------------------------------------------------

#gerando o relatorio em um arquivo txt chamado relatorio.txt(importante passar o diretorio onde deseja que seja amrmazenado o relatorio)
with open(r"C:\Users\sdietrich\Documents\Data science project\script python automação\autamatizar varias planilhas\relatorio.txt", 'w') as relatorio:
    relatorio.write(f'Printando o cabecalho da planilha 1 ==================================> {cabecalho_planilha1}'+'\n')
    relatorio.write(f'Printando a coluna que selecionamos na planilha 1 ====================> {coluna}'+'\n')
    relatorio.write(f'Quantidade total de pizza que foi vendida nas duas planilhas =========> {i}'+'\n')
    relatorio.write(f'Venda total das {i} pizza vendidas na duas planilhas ==================> {total}'+'\n')
    relatorio.write(f'Valor media de Pizza vendida se baseando nas duas planilha ===========> {total/i}'+'\n')

#-----------------------------------------------------------------------------------------------------------------------------
