from openpyxl import Workbook
import pandas as pd

# ler arquivo
df_origem = pd.read_excel(caminho_origem)

# Caminhos dos arquivos
caminho_origem = 'transacoes_financeiro_completo.xlsx'
caminho_destino = 'transacoes_financeiro_1_semestre.xlsx'

# Selecionar as colunas
colunas_necessarias = ['Data', 'Valor (R$)', 'Nota Fiscal', 'Categoria', 'Tipo de Transação']
df_origem = df_origem[colunas_necessarias]

# Exporta os dados para a planilha
df_origem.to_excel(caminho_destino, index=False)

print("Feito!")
