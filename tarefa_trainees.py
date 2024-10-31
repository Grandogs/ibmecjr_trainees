import pandas as pd


# Caminhos dos arquivos

caminho_origem = input(f'Digite o nome do arquivo de origem: ')
caminho_destino = input(f'Digite o nome do arquivo de destino: ')

def ler_arquivo(caminho_origem):
    df_origem = pd.read_excel(caminho_origem)
    return df_origem

# Selecionar as colunas
def selecionar_colunas(df_origem):
    colunas_necessarias = ['Data', 'Valor (R$)', 'Nota Fiscal', 'Categoria', 'Tipo de Transação']
    df_origem = df_origem[colunas_necessarias]
    return df_origem

# Converter a coluna "Data de transação" para o formato datetime (caso não esteja)
def converte_data(df_origem):
    df_origem['Data'] = pd.to_datetime(df_origem['Data'], errors='coerce')
    return df_origem
            
# Filtrar dados de datas
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
z = converte_data(y)
w = filtrar(z)
exporta(w, caminho_destino)

