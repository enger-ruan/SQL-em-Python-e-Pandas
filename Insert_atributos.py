import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

# crio um cursor ele serve para executar as instruções sql 

c = conn.cursor()

# ultilizo a variavel que defini como cursor, e dentro do execute eu passo a função SQL que quero ultilizar
c.execute('''INSERT INTO tb_products (id_product, name_product, price) 
                VALUES
                (1, 'Notebook', 2000),
                (2, 'Computador', 2000),
                (3, 'Tablet', 2000)
                
                ''')
conn.commit()

