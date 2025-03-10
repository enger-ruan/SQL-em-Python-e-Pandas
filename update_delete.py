import sqlite3
import pandas as pd

# crio um banco de dados sua conexão com o python
conn = sqlite3.connect('web.db')

# crio um cursor ele serve para executar as instruções sql 
c = conn.cursor()

# faço um update no valor especifico da minha tabela, passando o novo valor 218, e indentificado o local que quero alterar
# informando a coluna 'A'e o index 'B'
c.execute("UPDATE data SET A = 218 WHERE index_name = 'b'")

conn.commit()

c.close()
conn.close()