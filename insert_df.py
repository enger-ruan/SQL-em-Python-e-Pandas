import Create
import pandas as pd
import sqlite3


# Adicionando um dataframe ao meu banco de dados em uma tabela ja existente, isso pode ser bem util para adcionar linhas
# a uma tabela ja existente.

# cria a conexão com meu db
conn = sqlite3.connect('web.db')

# vou ultilizar meu df ja existente o df_data vou usalo como base para criar o df_data2 
# são o mesmo so que 2 e o 1 de traz para frente
df_data2 = Create.df_data.iloc[::-2]

# Adiciono meu df_data2 ao meu banco de dados na tabela data, e ultilizo o append para adicionar os dados
# na tabela ja existente
df_data2.to_sql('data', conn, if_exists='append')

conn.commit()
