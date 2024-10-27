from openpyxl import Workbook
import pandas as pd



# Caminhos dos arquivos
caminho_origem = 'transacoes_financeiro_completo.xlsx'
caminho_destino = 'transacoes_financeiro_1_semestre.xlsx'

# ler arquivo
df_origem = pd.read_excel(caminho_origem)

# Selecionar as colunas
colunas_necessarias = ['Data', 'Valor (R$)', 'Nota Fiscal', 'Categoria', 'Tipo de Transação']
df_origem = df_origem[colunas_necessarias]

"""•  Nesse caso vamos buscar os dados somente do primeiro semestre  do ano, o código precisa pegar as informações entre 
01/01/2024 até 30/06/2024.

•  Criar um arquivo .exe: O script precisa ser um arquivo executável com uma pequena interface visual pegando as  funcionalidades solicitadas.

"""

# Converter a coluna "Data de transação" para o formato datetime (caso não esteja)
# https://cursos.alura.com.br/forum/topico-filtrar-por-intervalo-de-data-tempo-no-pandas-93287

df_origem['Data'] = pd.to_datetime(df_origem['Data'], errors='coerce')


inicio = '2024-01-01 00:00:00'
fim = '2024-06-30 23:59:59'

# Filtrar dados de datas
#df_filtrado = df_origem[(df_origem['Data'] >= inicio) and (df_origem['Data'] <= fim)]
df_filtrado = df_origem[df_origem['Data'].between(inicio, fim)]

# Exporta os dados para a planilha
df_filtrado.to_excel(caminho_destino, index=False)

print("Feito!")
