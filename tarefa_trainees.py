from openpyxl import Workbook
import pandas as pd


# Caminhos dos arquivos
try:
    caminho_origem = input(f'Digite o nome do arquivo de origem: ')
    caminho_destino = input(f'Digite o nome do arquivo de destino: ')
except ValueError:
        print("Erro: Entrada inválida! Por favor, digite um nome de arquivo completo.")

#ler arquivo
def ler_arquivo(caminho_origem):
    df_origem = pd.read_excel(caminho_origem)
    return df_origem

# Selecionar as colunas

def selecionar_colunas(df_origem):
    colunas_necessarias = ['Data', 'Valor (R$)', 'Nota Fiscal', 'Categoria', 'Tipo de Transação']
    df_origem = df_origem[colunas_necessarias]
    return df_origem

"""•  Nesse caso vamos buscar os dados somente do primeiro semestre  do ano, o código precisa pegar as informações entre 
01/01/2024 até 30/06/2024.

•  Criar um arquivo .exe: O script precisa ser um arquivo executável com uma pequena interface visual pegando as  funcionalidades solicitadas.
"""

# Converter a coluna "Data de transação" para o formato datetime (caso não esteja)
# https://cursos.alura.com.br/forum/topico-filtrar-por-intervalo-de-data-tempo-no-pandas-93287

def converte_data(df_origem):
    df_origem['Data'] = pd.to_datetime(df_origem['Data'], errors='coerce')
    return df_origem

def validacao(df_origem):
    coluna_data_invalida = []
    coluna_data_invalida.append(df_origem['Data'].isna())
    coluna_data_invalida.append(df_origem['Valor (R$)'].isna())
    coluna_data_invalida.append(df_origem['Nota Fiscal'].isna())
    coluna_data_invalida.append(df_origem['Categoria'].isna())
    coluna_data_invalida.append(df_origem['Tipo de Transação'].isna())

    for x in coluna_data_invalida:
        dados_nulos = 0
        if x is True:
            dados_nulos + 1
            print("tem x valoer nulos no banco de dados")
    print('verificação completa')
        
            
# Filtrar dados de datas
#df_filtrado = df_origem[(df_origem['Data'] >= inicio) and (df_origem['Data'] <= fim)]
def filtrar(df_origem):
    inicio = '2024-01-01 00:00:00'
    fim = '2024-06-30 23:59:59'
    df_filtrado = df_origem[df_origem['Data'].between(inicio, fim)]
    return df_filtrado

# Exporta os dados para a planilha
def exporta(df_filtrado, caminho_destino):
    df_filtrado.to_excel(caminho_destino, index=False)
    print("Feito!")

# chamando funções
x =  ler_arquivo(caminho_origem)

y = selecionar_colunas(x)
validacao(y)
z = converte_data(y)
w = filtrar(z)
exporta(w, caminho_destino)

