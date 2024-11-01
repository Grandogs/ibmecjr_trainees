# ibmecjr_trainees

Resumo
O código recebe dois arquivos e exporta os dados do primeiro documento para o segundo automaticamente por meio de um executável.


Desafios 
 Preenchimento automático: Os dados precisam ser preenchidos automaticamente no momento que o script rodar.

• Validação de Dados: Verificar se todos os campos estão preenchidos corretamente (data, valor, categoria, tipo de transação e  nota fiscal).
Data de transação
Valor 
Nota fiscal
Categoria 
Tipo de transação

•  Nesse caso vamos buscar os dados somente do primeiro semestre  do ano, o código precisa pegar as informações entre 01/01/2024 até 30/06/2024.

•  Criar um arquivo .exe: O script precisa ser um arquivo executável com uma pequena interface visual pegando as  funcionalidades solicitadas.





Define o caminho dos arquivos:
Define o caminho do arquivo Excel de origem e do arquivo Excel de destino.

Lê a planilha:
Carrega o arquivo de origem em um DataFrame.

Converte a coluna de data:
Converte a coluna Data de transação para o tipo datetime, garantindo que todos os dados estejam no formato correto de data.

Define o intervalo de datas e horas:
Especifica o intervalo de datas e horas para o filtro. No exemplo, o intervalo vai de 01/01/2024 00:00:00 até 30/06/2024 23:59:59.

Filtra os dados no intervalo de tempo:
Filtra as linhas cuja Data de transação está dentro do intervalo definido.


Exporta os dados filtrados:
Salva os dados filtrados em uma nova planilha Excel no caminho de destino.