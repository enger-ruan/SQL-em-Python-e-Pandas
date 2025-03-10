import sqlite3
import pandas as pd

# crio um banco de dados sua conexão com o python
conn = sqlite3.connect('web.db')

# abro o arquivo csv o tranformando em um dataframe
df_data =  pd.read_csv('bd_data.csv', index_col=0)
print(df_data)

# defino o nome do meu index
df_data.index = df_data.index.rename('index_name')

# exporto o meu conjunto de dados para o banco de dados sql que criei
df_data.to_sql('data', conn, if_exists='replace', index_label='index_name')

# crio um cursor ele serve para executar as instruções sql 
c = conn.cursor()

# ultilizo a variavel que defini como cursor, e dentro de execute eu passo a função SQL que quero ultilizar
'''
c.execute("CREATE TABLE tb_products (id_product INTEGER PRIMARY KEY, name_product TEXT, price REAL)")
c.commit()
'''